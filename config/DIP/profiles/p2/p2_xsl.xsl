<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:xs="http://www.w3.org/2001/XMLSchema"
                xmlns:array="http://www.w3.org/2005/xpath-functions/array"
                xmlns:map="http://www.w3.org/2005/xpath-functions/map"
                xmlns:math="http://www.w3.org/2005/xpath-functions/math"
                xmlns:dips="http://dips.bundesarchiv.de/schema"
                xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:gen="gen"
                exclude-result-prefixes="#all"
                expand-text="yes"
                version="3.0">

    <xsl:output method="xml" indent="yes" encoding="UTF-8" standalone="yes"/>
    <xsl:mode on-no-match="shallow-copy"/>

    <xsl:variable name="json" select="parse-json(unparsed-text('./vars.json'))"/>
    <!-- <xsl:variable name="vze" select="./vze.xml"/> -->
    <xsl:variable name="aips" select="collection('./aips/')"/>

    <xsl:function name="gen:objects-by-iid">
        <xsl:param name="iid"/>
        <xsl:for-each select="$aips[last()]//dips:object/dips:objectIdentifier">
            <xsl:variable name="t" select="dips:objectIdentifierType"/>
            <xsl:variable name="v" select="dips:objectIdentifierValue"/>
            <xsl:if test="$aips//dips:intellectualEntity/*[dips:IID = $iid
            and .//dips:linkingObjectIdentifierType = $t
            and .//dips:linkingObjectIdentifierValue = $v]">
            <linkingObject xmlns="http://dips.bundesarchiv.de/schema">
                <linkingObjectIdentifier>
                    <linkingObjectIdentifierType><xsl:value-of select="$t"/></linkingObjectIdentifierType>
                    <linkingObjectIdentifierValue><xsl:value-of select="$v"/></linkingObjectIdentifierValue>
                </linkingObjectIdentifier>
                <xsl:for-each select="$aips">
                    <xsl:if test=".//dips:intellectualEntity/*[dips:IID = $iid
                        and .//dips:linkingObjectIdentifierType = $t
                        and .//dips:linkingObjectIdentifierValue = $v]">
                        <linkingAIPIdentifier><xsl:value-of select=".//dips:AIPID"/></linkingAIPIdentifier>
                    </xsl:if>
                </xsl:for-each>
            </linkingObject>
            </xsl:if>
        </xsl:for-each>
    </xsl:function>

    <xsl:template match="/*" mode="#all">
        <dips_dip>
            <xsl:namespace name="xsi" select="'http://www.w3.org/2001/XMLSchema-instance'"/>
            <xsl:attribute name="xsi:schemaLocation" select="concat('http://dips.bundesarchiv.de/schema', ' ', map:get($json, 'schema'))"/>
            <DIP>
                <DIPID>
                    <xsl:value-of select="map:get($json, 'id')"/>
                </DIPID>
                <type>
                    <xsl:value-of select="map:get($json, 'type')"/>
                </type>
                <profileNumber>
                    <xsl:value-of select="map:get($json, 'profileNumber')"/>
                </profileNumber>
                <profileDescription>
                    <xsl:value-of select="map:get($json, 'profileDescription')"/>
                </profileDescription>
                <profileVersion>
                    <xsl:value-of select="map:get($json, 'profileVersion')"/>
                </profileVersion>
                <issuedBy>
                    <xsl:value-of select="map:get($json, 'issuedBy')"/>
                </issuedBy>
                <generatorName>
                    <xsl:value-of select="map:get($json, 'generatorName')"/>
                </generatorName>
                <generatorVersion>
                    <xsl:value-of select="map:get($json, 'generatorVersion')"/>
                </generatorVersion>
                <generationDateTime>
                    <xsl:value-of select="map:get($json, 'generationDate')"/>
                </generationDateTime>
            </DIP>
            <VZE></VZE>
            <intellectualEntity xmlns="http://dips.bundesarchiv.de/schema">
                <xsl:variable name="ie" select="$aips[1]//dips:intellectualEntity"/>
                <xsl:copy-of select="$ie/@*|
                $ie/dips:IEID|
                $ie/dips:title|
                $ie/dips:type|
                $ie/dips:additionalDescriptiveMetadata"/>
                <extDescriptiveMetadataItem>
                    <xsl:copy-of select="$ie/dips:extDescriptiveMetadataItem/@*|
                        $ie/dips:extDescriptiveMetadataItem/node()[not(self::dips:linkingObjectIdentifier)]"/>
                        <xsl:copy-of select="gen:objects-by-iid($ie/dips:extDescriptiveMetadataItem/dips:IID)"/>
                </extDescriptiveMetadataItem>
                <xsl:for-each select="$ie/dips:item">
                    <item>
                        <xsl:copy-of select="@*|node()[not(self::dips:linkingObjectIdentifier)]"/>
                        <xsl:copy-of select="gen:objects-by-iid(dips:IID)"/>
                    </item>
                </xsl:for-each>
                <xsl:copy-of select="$ie/dips:date|
                $ie/dips:referenceNumber|
                $ie/dips:structure|
                $ie/dips:description|
                $ie/dips:ID_Archivsignatur_IE|
                $ie/dips:reference"/>
            </intellectualEntity>
            <dip_technical>
                <admin xmlns="http://dips.bundesarchiv.de/schema">
                    <xsl:variable name="admin" select="$aips[1]//dips:admin"/>
                    <xsl:copy-of select="$admin/@*"/>
                    <xsl:copy-of select="$admin/dips:transaction/node()[not(self::dips:transactionIdentifier)
                        and not(self::dips:transactionNumber)
                        and not(self::dips:transactionType)]
                        |$admin/dips:transaction/@*"/>
                    <xsl:copy-of select="$admin/dips:date|
                        $admin/dips:provenance|
                        $admin/dips:producer|
                        $admin/dips:note|
                        $admin/dips:submissionContent|
                        $admin/dips:date|
                        $admin/dips:hybrid|
                        $admin/dips:additionalDescriptiveMetadata|
                        $admin/dips:fondsNumber"/>
                </admin>
                <aips>
                    <xsl:for-each select="$aips">
                        <AIP xmlns="http://dips.bundesarchiv.de/schema">
                            <xsl:copy-of select="//dips:AIP/node()|//dips:AIP/@*"/>
                            <xsl:for-each select="//dips:intellectualEntity//dips:linkingObjectIdentifier">
                                <linkingObjectIdentifier xmlns="http://dips.bundesarchiv.de/schema">
                                    <xsl:copy-of select="node()|@*"/>
                                </linkingObjectIdentifier>
                            </xsl:for-each>
                        </AIP>
                    </xsl:for-each>
                </aips>
                <xsl:for-each select="$aips[last()]//dips:object">
                    <object xmlns="http://dips.bundesarchiv.de/schema">
                        <xsl:copy-of select="@*"/>
                        <xsl:copy-of select="dips:objectIdentifier | dips:preservationLevel | dips:objectCategory"/>
                        <objectCharacteristics>
                            <xsl:variable name="oc" select="dips:objectCharacteristics"/>
                            <xsl:copy-of select="$oc/dips:compositionLevel|
                                $oc/dips:fixity|
                                $oc/dips:size|
                                $oc/@*"/>
                            <format>
                                <formatDesignation>
                                    <xsl:variable name="fd" select="$oc/dips:format/dips:formatDesignation"/>
                                    <xsl:copy-of select="$fd/dips:formatName|
                                        $fd/dips:formatVersion|
                                        $fd/dips:textEncoding|
                                        $fd/@*"/>
                                </formatDesignation>
                            </format>
                            <xsl:copy-of select="$oc/dips:compositionLevel|
                                $oc/dips:codec|
                                $oc/dips:additionalDescriptiveMetadata|
                                $oc/dips:significantProperties|
                                $oc/dips:creatingApplication|
                                $oc/dips:originalName|
                                $oc/dips:environment|
                                $oc/dips:relationship|
                                $oc/dips:initialName"/>
                        </objectCharacteristics>
                        <xsl:for-each select="dips:linkingEventIdentifier">
                            <xsl:variable name="t" select="dips:linkingEventIdentifierType"/>
                            <xsl:variable name="v" select=".//dips:linkingEventIdentifierValue"/>
                            <xsl:if test="/descendant::dips:event[not(dips:eventType/text() = 'formatRecognition')
                            and not(dips:eventType/text() = 'validation')
                            and dips:eventIdentifier/dips:eventIdentifierType = $t/text()
                            and dips:eventIdentifier/dips:eventIdentifierValue = $v/text()]">
                                <linkingEventIdentifier>
                                    <xsl:copy-of select="node()|@*"/>
                                </linkingEventIdentifier>
                            </xsl:if>
                        </xsl:for-each>
                    </object>
                </xsl:for-each>
                <xsl:copy-of select="$aips[last()]//dips:event[not(dips:eventType/text() = 'formatRecognition')
                    and not(dips:eventType/text() = 'validation')]"/>
                <xsl:for-each select="$aips[last()]//dips:agent">
                    <xsl:variable name="t" select=".//dips:agentIdentifierType"/>
                    <xsl:variable name="v" select=".//dips:agentIdentifierValue"/>
                    <xsl:if test="/descendant::dips:event[not(dips:eventType/text() = 'formatRecognition')
                    and not(dips:eventType/text() = 'validation')
                    and dips:linkingAgentIdentifier/dips:linkingAgentIdentifierType = $t/text()
                    and dips:linkingAgentIdentifier/dips:linkingAgentIdentifierValue = $v/text()]">
                        <agent>
                            <xsl:copy-of select="node()|@*"/>
                        </agent>
                    </xsl:if>
                </xsl:for-each>
                <xsl:copy-of select="$aips[last()]//dips:structure"/>
            </dip_technical>
        </dips_dip>
    </xsl:template>
</xsl:stylesheet>
