<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<xsl:stylesheet version="2.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:ma="http://www.sec.state.ma.us/arc/digital/archives_dc_schema/v1">
	
	<xsl:output method="xml" indent="yes"/>
	
	<xsl:template match="@*|node()">
	 <xsl:copy>
	  <xsl:apply-templates select="@*|node()"/>
	 </xsl:copy>
	</xsl:template>
	
	<xsl:template match="/vitalRecord">
		<xsl:for-each select="/vitalRecord/record">
			<xsl:result-document href="{filename}.metadata">
				<ma:record>
					<ma:dc>
						<ma:title><xsl:value-of select="title"/></ma:title>
						<ma:creator>Massachusetts. Registry of Vital Records and Statistics</ma:creator>
						<ma:contributor></ma:contributor>
						<ma:publisher></ma:publisher>
						<ma:description><xsl:value-of select="description"/></ma:description>
						<ma:description>Deaths Volume 21: Everett January 13 - December 30, 1916 of series 1411, Registers of vital records, 1841-1925, was digitized on September 15, 2011 by FamilySearch. Originals are located at the Massachusetts Archives.</ma:description>
						<ma:identifier><xsl:value-of select="recordGroup"/></ma:identifier>
						<ma:identifier><xsl:value-of select="series"/></ma:identifier>
						<ma:identifier><xsl:value-of select="fileUnit"/></ma:identifier>
						<ma:identifier><xsl:value-of select="item"/></ma:identifier>
						<ma:identifier>Registers of vital records, 1841-1925. (HS6.07 / Series 1411) Massachusetts Archives. Boston, MA. Accessed [insert date accessed in format DD MM YYYY]. [insert URL of resource].</ma:identifier>
						<ma:date><xsl:value-of select="date"/></ma:date>
						<ma:type>Text</ma:type>
						<ma:format>vital statistics records</ma:format>
						<ma:subject>Registers of births, etc.--Massachusetts</ma:subject>
						<ma:subject>Massachusetts--Politics and government--1775-1865</ma:subject>
						<ma:subject>Massachusetts--Politics and government--1865-1950</ma:subject>
						<ma:coverage><xsl:value-of select="coverage"/></ma:coverage>
						<ma:source></ma:source>
						<ma:relation>Part of Collection: Record Group HS6.07 (Registry of Vital Records and Statistics), Series 1411 (Registers of vital records, 1841-1925)</ma:relation>
						<ma:language>en</ma:language>
						<ma:rights>none</ma:rights>
						<ma:rights>Those records created by Massachusetts government agencies and institutions held by the Massachusetts Archives are not copyrighted and are available for public use. Copyright for materials submitted to state agencies may be held by the person or organization that created the document. Patrons are responsible for clearing copyright on such materials. For more information on copyright law, please see the U.S. Copyright Office's web page at lcweb.loc.gov/copyright.</ma:rights>
					</ma:dc>
				</ma:record>
			</xsl:result-document>
		</xsl:for-each>
	</xsl:template>	
</xsl:stylesheet>
