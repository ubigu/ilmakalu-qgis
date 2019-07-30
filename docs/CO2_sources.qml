<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis minScale="1e+08" simplifyAlgorithm="0" simplifyLocal="1" styleCategories="AllStyleCategories" labelsEnabled="0" simplifyMaxScale="1" readOnly="0" simplifyDrawingTol="1" hasScaleBasedVisibilityFlag="0" simplifyDrawingHints="0" version="3.6.2-Noosa" maxScale="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 enableorderby="0" symbollevels="1" type="RuleRenderer" forceraster="0">
    <rules key="{4137ce98-8dc0-4a23-ac5a-a4b6ac06232e}">
      <rule filter=" &quot;lammitys_tco2&quot; > &quot;vesi_tco2&quot; AND   &quot;lammitys_tco2&quot;  >  &quot;jaahdytys_tco2&quot;  AND   &quot;lammitys_tco2&quot;  >  &quot;sahko_yht&quot; AND   &quot;lammitys_tco2&quot;  >  &quot;liikenne_yht&quot;  AND  &quot;lammitys_tco2&quot;  >    &quot;korjaussaneeraus_tco2&quot; " symbol="0" label="Tilojen lämmitys" key="{81e482bf-6bad-4a8d-abf5-f43f0c63eb35}"/>
      <rule filter="&quot;sahko_yht&quot; > &quot;vesi_tco2&quot; AND   &quot;sahko_yht&quot; > &quot;lammitys_tco2&quot;  AND   &quot;sahko_yht&quot;  >  &quot;jaahdytys_tco2&quot; AND   &quot;sahko_yht&quot; >   &quot;liikenne_yht&quot;  AND    &quot;sahko_yht&quot; >  &#xd;&#xa;&quot;korjaussaneeraus_tco2&quot; " symbol="1" label="Sähkö yhteensä" key="{f782f537-4068-4299-a776-3c26986e0399}"/>
      <rule filter=" &quot;liikenne_yht&quot;> &quot;vesi_tco2&quot; AND     &quot;liikenne_yht&quot;> &quot;lammitys_tco2&quot;  AND     &quot;liikenne_yht&quot;>  &quot;jaahdytys_tco2&quot; AND     &quot;liikenne_yht&quot;>  &quot;sahko_yht&quot;  AND   &quot;liikenne_yht&quot;>   &quot;korjaussaneeraus_tco2&quot; " symbol="2" label="Liikenne yhteensä" key="{6a0cb3ef-bd69-426b-ae31-3971fac9fb3f}"/>
      <rule filter=" &quot;korjaussaneeraus_tco2&quot; > &quot;vesi_tco2&quot; AND        &quot;korjaussaneeraus_tco2&quot; > &quot;lammitys_tco2&quot;  AND        &quot;korjaussaneeraus_tco2&quot;>  &quot;jaahdytys_tco2&quot; AND       &quot;korjaussaneeraus_tco2&quot; >  &quot;sahko_yht&quot;  AND   &quot;korjaussaneeraus_tco2&quot;>    &quot;liikenne_yht&quot;  " symbol="3" label="Korjaussaneeraus" key="{c0f03c0e-9982-4ba6-9847-444a65bed735}"/>
    </rules>
    <symbols>
      <symbol clip_to_extent="1" force_rhr="0" name="0" alpha="1" type="fill">
        <layer pass="1" enabled="1" class="CentroidFill" locked="0">
          <prop k="point_on_all_parts" v="0"/>
          <prop k="point_on_surface" v="1"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@0@0" alpha="1" type="marker">
            <layer pass="0" enabled="1" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="255,78,0,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="square"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="79,79,79,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.2"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="1"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="1" alpha="1" type="fill">
        <layer pass="1" enabled="1" class="CentroidFill" locked="0">
          <prop k="point_on_all_parts" v="1"/>
          <prop k="point_on_surface" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@1@0" alpha="1" type="marker">
            <layer pass="0" enabled="1" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="43,43,43,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="triangle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_style" v="no"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="1.6"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="2" alpha="1" type="fill">
        <layer pass="1" enabled="1" class="CentroidFill" locked="0">
          <prop k="point_on_all_parts" v="1"/>
          <prop k="point_on_surface" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@2@0" alpha="1" type="marker">
            <layer pass="0" enabled="1" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="170,0,255,0"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="circle"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="170,0,255,255"/>
              <prop k="outline_style" v="solid"/>
              <prop k="outline_width" v="0.4"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="1.2"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
      <symbol clip_to_extent="1" force_rhr="0" name="3" alpha="1" type="fill">
        <layer pass="1" enabled="1" class="CentroidFill" locked="0">
          <prop k="point_on_all_parts" v="1"/>
          <prop k="point_on_surface" v="0"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
          <symbol clip_to_extent="1" force_rhr="0" name="@3@0" alpha="1" type="marker">
            <layer pass="0" enabled="1" class="SimpleMarker" locked="0">
              <prop k="angle" v="0"/>
              <prop k="color" v="9,30,16,255"/>
              <prop k="horizontal_anchor_point" v="1"/>
              <prop k="joinstyle" v="bevel"/>
              <prop k="name" v="diamond"/>
              <prop k="offset" v="0,0"/>
              <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="offset_unit" v="MM"/>
              <prop k="outline_color" v="35,35,35,255"/>
              <prop k="outline_style" v="no"/>
              <prop k="outline_width" v="0"/>
              <prop k="outline_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="outline_width_unit" v="MM"/>
              <prop k="scale_method" v="diameter"/>
              <prop k="size" v="1.2"/>
              <prop k="size_map_unit_scale" v="3x:0,0,0,0,0,0"/>
              <prop k="size_unit" v="MM"/>
              <prop k="vertical_anchor_point" v="1"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" value="" type="QString"/>
                  <Option name="properties"/>
                  <Option name="type" value="collection" type="QString"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <labeling type="simple">
    <settings>
      <text-style fontFamily="Verdana" useSubstitutions="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" fontWeight="50" fontStrikeout="0" textColor="31,30,29,255" fontCapitals="0" fontSizeUnit="Point" multilineHeight="1" fontWordSpacing="0" fontUnderline="0" fieldName="summa" previewBkgrdColor="#ffffff" fontLetterSpacing="0" textOpacity="1" blendMode="0" fontItalic="0" fontSize="5" isExpression="0" namedStyle="Normal">
        <text-buffer bufferOpacity="1" bufferBlendMode="0" bufferColor="255,255,255,255" bufferNoFill="1" bufferJoinStyle="128" bufferDraw="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0" bufferSize="1" bufferSizeUnits="MM"/>
        <background shapeOffsetY="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSVGFile="" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeBorderWidthUnit="MM" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeFillColor="255,255,255,255" shapeRotation="0" shapeBorderColor="128,128,128,255" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiUnit="MM" shapeRadiiX="0" shapeRotationType="0" shapeDraw="0" shapeBlendMode="0" shapeSizeType="0" shapeSizeX="0" shapeType="0" shapeOffsetUnit="MM" shapeSizeY="0" shapeSizeUnit="MM" shapeBorderWidth="0" shapeOpacity="1" shapeJoinStyle="64" shapeRadiiY="0" shapeOffsetX="0"/>
        <shadow shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowRadiusAlphaOnly="0" shadowOpacity="0" shadowUnder="0" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowRadius="0" shadowOffsetUnit="MM" shadowColor="0,0,0,255" shadowOffsetDist="1" shadowOffsetGlobal="1" shadowRadiusUnit="MM" shadowScale="100" shadowDraw="0" shadowOffsetAngle="135"/>
        <substitutions/>
      </text-style>
      <text-format useMaxLineLengthForAutoWrap="1" wrapChar="" leftDirectionSymbol="&lt;" decimals="1" rightDirectionSymbol=">" addDirectionSymbol="0" autoWrapLength="3" formatNumbers="1" placeDirectionSymbol="0" multilineAlign="4294967295" reverseDirectionSymbol="0" plussign="0"/>
      <placement rotationAngle="0" preserveRotation="1" offsetUnits="MapUnit" priority="10" repeatDistanceUnits="MM" centroidWhole="1" dist="0" fitInPolygonOnly="0" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" placementFlags="10" yOffset="60" distUnits="MM" distMapUnitScale="3x:0,0,0,0,0,0" xOffset="0" labelOffsetMapUnitScale="3x:0,0,0,0,0,0" placement="1" offsetType="0" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" maxCurvedCharAngleIn="25" quadOffset="7" centroidInside="1" repeatDistance="0" maxCurvedCharAngleOut="-25"/>
      <rendering mergeLines="0" maxNumLabels="2000" obstacle="1" fontMaxPixelSize="10000" scaleMax="25000" obstacleType="0" drawLabels="1" displayAll="1" labelPerPart="0" zIndex="0" obstacleFactor="1" fontMinPixelSize="3" scaleMin="1000" upsidedownLabels="0" minFeatureSize="0" scaleVisibility="1" limitNumLabels="0" fontLimitPixelSize="0"/>
      <dd_properties>
        <Option type="Map">
          <Option name="name" value="" type="QString"/>
          <Option name="properties"/>
          <Option name="type" value="collection" type="QString"/>
        </Option>
      </dd_properties>
    </settings>
  </labeling>
  <customproperties>
    <property value="fid" key="dualview/previewExpressions"/>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <LinearlyInterpolatedDiagramRenderer classificationAttributeExpression=" &quot;vesi_tco2&quot; + &quot;lammitys_tco2&quot; + &quot;jaahdytys_tco2&quot; + &quot;kiinteistosahko_tco2&quot; + &quot;sahko_kotitaloudet_tco2&quot; + &quot;sahko_palv_tco2&quot; + &quot;sahko_tv_tco2&quot; + &quot;hloliikenne_ap_tco2&quot; + &quot;hloliikenne_tp_tco2&quot; + &quot;tvliikenne_tco2&quot; + &quot;palvliikenne_tco2&quot; + &quot;korjaussaneeraus_tco2&quot; " diagramType="Pie" upperHeight="10" upperValue="12138.6" lowerValue="0" attributeLegend="1" lowerHeight="0" lowerWidth="0" upperWidth="10">
    <DiagramCategory diagramOrientation="Up" barWidth="5" minScaleDenominator="1000" lineSizeType="MM" width="15" penAlpha="255" backgroundColor="#ffffff" rotationOffset="270" lineSizeScale="3x:0,0,0,0,0,0" scaleBasedVisibility="1" scaleDependency="Area" maxScaleDenominator="50000" sizeScale="3x:0,0,0,0,0,0" minimumSize="3" enabled="0" backgroundAlpha="255" height="15" penColor="#ffffff" penWidth="0.1" labelPlacementMethod="XHeight" opacity="1" sizeType="MM">
      <fontProperties description="MS Shell Dlg 2,7.8,-1,5,50,0,0,0,0,0" style=""/>
      <attribute label="Lämmitys" field="lammitys_tco2" color="#ca4d41"/>
      <attribute label="Vesi" field="vesi_tco2" color="#418aca"/>
      <attribute label="Henkilöliikenne, ap" field="hloliikenne_ap_tco2" color="#c551bc"/>
      <attribute label="Sähkö, kotitaloudet" field="sahko_kotitaloudet_tco2" color="#ecff3b"/>
      <attribute label="Palveluliikenne" field="palvliikenne_tco2" color="#745d7c"/>
      <attribute label="Sähkö, palvelut" field="sahko_palv_tco2" color="#decd98"/>
      <attribute label="Liikenne, tv" field="tvliikenne_tco2" color="#661f98"/>
      <attribute label="Sähkö, tv" field="sahko_tv_tco2" color="#bbf7d6"/>
      <attribute label="Kiinteistösähkö" field="kiinteistosahko_tco2" color="#3a2f6c"/>
      <attribute label="Henkilöliikenne, tp" field="hloliikenne_tp_tco2" color="#4dee3b"/>
      <attribute label="Korjaussaneeraus" field="korjaussaneeraus_tco2" color="#d6a4ff"/>
      <attribute label="Jäähdytys" field="jaahdytys_tco2" color="#51c7bc"/>
    </DiagramCategory>
  </LinearlyInterpolatedDiagramRenderer>
  <DiagramLayerSettings priority="10" placement="4" obstacle="0" zIndex="0" showAll="1" linePlacementFlags="18" dist="0">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="id_0">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="xyind">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="vuosi">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="vesi_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lammitys_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="jaahdytys_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="kiinteistosahko_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_kotitaloudet_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_palv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_tv_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="hloliikenne_ap_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="hloliikenne_tp_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="tvliikenne_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="palvliikenne_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="korjaussaneeraus_tco2">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="summa">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sahko_yht">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="liikenne_yht">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias index="0" name="" field="id_0"/>
    <alias index="1" name="" field="id"/>
    <alias index="2" name="" field="fid"/>
    <alias index="3" name="" field="xyind"/>
    <alias index="4" name="" field="vuosi"/>
    <alias index="5" name="" field="vesi_tco2"/>
    <alias index="6" name="" field="lammitys_tco2"/>
    <alias index="7" name="" field="jaahdytys_tco2"/>
    <alias index="8" name="" field="kiinteistosahko_tco2"/>
    <alias index="9" name="" field="sahko_kotitaloudet_tco2"/>
    <alias index="10" name="" field="sahko_palv_tco2"/>
    <alias index="11" name="" field="sahko_tv_tco2"/>
    <alias index="12" name="" field="hloliikenne_ap_tco2"/>
    <alias index="13" name="" field="hloliikenne_tp_tco2"/>
    <alias index="14" name="" field="tvliikenne_tco2"/>
    <alias index="15" name="" field="palvliikenne_tco2"/>
    <alias index="16" name="" field="korjaussaneeraus_tco2"/>
    <alias index="17" name="" field="summa"/>
    <alias index="18" name="" field="sahko_yht"/>
    <alias index="19" name="" field="liikenne_yht"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="id_0" expression="" applyOnUpdate="0"/>
    <default field="id" expression="" applyOnUpdate="0"/>
    <default field="fid" expression="" applyOnUpdate="0"/>
    <default field="xyind" expression="" applyOnUpdate="0"/>
    <default field="vuosi" expression="" applyOnUpdate="0"/>
    <default field="vesi_tco2" expression="" applyOnUpdate="0"/>
    <default field="lammitys_tco2" expression="" applyOnUpdate="0"/>
    <default field="jaahdytys_tco2" expression="" applyOnUpdate="0"/>
    <default field="kiinteistosahko_tco2" expression="" applyOnUpdate="0"/>
    <default field="sahko_kotitaloudet_tco2" expression="" applyOnUpdate="0"/>
    <default field="sahko_palv_tco2" expression="" applyOnUpdate="0"/>
    <default field="sahko_tv_tco2" expression="" applyOnUpdate="0"/>
    <default field="hloliikenne_ap_tco2" expression="" applyOnUpdate="0"/>
    <default field="hloliikenne_tp_tco2" expression="" applyOnUpdate="0"/>
    <default field="tvliikenne_tco2" expression="" applyOnUpdate="0"/>
    <default field="palvliikenne_tco2" expression="" applyOnUpdate="0"/>
    <default field="korjaussaneeraus_tco2" expression="" applyOnUpdate="0"/>
    <default field="summa" expression="" applyOnUpdate="0"/>
    <default field="sahko_yht" expression="" applyOnUpdate="0"/>
    <default field="liikenne_yht" expression="" applyOnUpdate="0"/>
  </defaults>
  <constraints>
    <constraint notnull_strength="1" exp_strength="0" unique_strength="1" constraints="3" field="id_0"/>
    <constraint notnull_strength="1" exp_strength="0" unique_strength="1" constraints="3" field="id"/>
    <constraint notnull_strength="1" exp_strength="0" unique_strength="1" constraints="3" field="fid"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="xyind"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="vuosi"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="vesi_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="lammitys_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="jaahdytys_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="kiinteistosahko_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="sahko_kotitaloudet_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="sahko_palv_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="sahko_tv_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="hloliikenne_ap_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="hloliikenne_tp_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="tvliikenne_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="palvliikenne_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="korjaussaneeraus_tco2"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="summa"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="sahko_yht"/>
    <constraint notnull_strength="0" exp_strength="0" unique_strength="0" constraints="0" field="liikenne_yht"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="id_0"/>
    <constraint exp="" desc="" field="id"/>
    <constraint exp="" desc="" field="fid"/>
    <constraint exp="" desc="" field="xyind"/>
    <constraint exp="" desc="" field="vuosi"/>
    <constraint exp="" desc="" field="vesi_tco2"/>
    <constraint exp="" desc="" field="lammitys_tco2"/>
    <constraint exp="" desc="" field="jaahdytys_tco2"/>
    <constraint exp="" desc="" field="kiinteistosahko_tco2"/>
    <constraint exp="" desc="" field="sahko_kotitaloudet_tco2"/>
    <constraint exp="" desc="" field="sahko_palv_tco2"/>
    <constraint exp="" desc="" field="sahko_tv_tco2"/>
    <constraint exp="" desc="" field="hloliikenne_ap_tco2"/>
    <constraint exp="" desc="" field="hloliikenne_tp_tco2"/>
    <constraint exp="" desc="" field="tvliikenne_tco2"/>
    <constraint exp="" desc="" field="palvliikenne_tco2"/>
    <constraint exp="" desc="" field="korjaussaneeraus_tco2"/>
    <constraint exp="" desc="" field="summa"/>
    <constraint exp="" desc="" field="sahko_yht"/>
    <constraint exp="" desc="" field="liikenne_yht"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig sortOrder="0" actionWidgetStyle="dropDown" sortExpression="&quot;liikenne_yht&quot;">
    <columns>
      <column width="-1" name="fid" hidden="0" type="field"/>
      <column width="-1" name="xyind" hidden="0" type="field"/>
      <column width="-1" name="vuosi" hidden="0" type="field"/>
      <column width="-1" name="vesi_tco2" hidden="0" type="field"/>
      <column width="-1" name="lammitys_tco2" hidden="0" type="field"/>
      <column width="-1" name="jaahdytys_tco2" hidden="0" type="field"/>
      <column width="-1" name="kiinteistosahko_tco2" hidden="0" type="field"/>
      <column width="202" name="sahko_kotitaloudet_tco2" hidden="0" type="field"/>
      <column width="-1" name="sahko_palv_tco2" hidden="0" type="field"/>
      <column width="-1" name="sahko_tv_tco2" hidden="0" type="field"/>
      <column width="-1" name="hloliikenne_ap_tco2" hidden="0" type="field"/>
      <column width="-1" name="hloliikenne_tp_tco2" hidden="0" type="field"/>
      <column width="-1" name="tvliikenne_tco2" hidden="0" type="field"/>
      <column width="-1" name="palvliikenne_tco2" hidden="0" type="field"/>
      <column width="202" name="korjaussaneeraus_tco2" hidden="0" type="field"/>
      <column width="-1" name="summa" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
      <column width="-1" name="id" hidden="0" type="field"/>
      <column width="-1" name="sahko_yht" hidden="0" type="field"/>
      <column width="-1" name="liikenne_yht" hidden="0" type="field"/>
      <column width="-1" name="id_0" hidden="0" type="field"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="fid" editable="1"/>
    <field name="hloliikenne_ap_tco2" editable="1"/>
    <field name="hloliikenne_tp_tco2" editable="1"/>
    <field name="id" editable="1"/>
    <field name="id_0" editable="1"/>
    <field name="jaahdytys_tco2" editable="1"/>
    <field name="kiinteistosahko_tco2" editable="1"/>
    <field name="korjaussaneeraus_tco2" editable="1"/>
    <field name="lammitys_tco2" editable="1"/>
    <field name="liikenne_yht" editable="1"/>
    <field name="palvliikenne_tco2" editable="1"/>
    <field name="sahko_kotitaloudet_tco2" editable="1"/>
    <field name="sahko_palv_tco2" editable="1"/>
    <field name="sahko_tv_tco2" editable="1"/>
    <field name="sahko_yht" editable="1"/>
    <field name="summa" editable="1"/>
    <field name="tvliikenne_tco2" editable="1"/>
    <field name="vesi_tco2" editable="1"/>
    <field name="vuosi" editable="1"/>
    <field name="xyind" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="fid" labelOnTop="0"/>
    <field name="hloliikenne_ap_tco2" labelOnTop="0"/>
    <field name="hloliikenne_tp_tco2" labelOnTop="0"/>
    <field name="id" labelOnTop="0"/>
    <field name="id_0" labelOnTop="0"/>
    <field name="jaahdytys_tco2" labelOnTop="0"/>
    <field name="kiinteistosahko_tco2" labelOnTop="0"/>
    <field name="korjaussaneeraus_tco2" labelOnTop="0"/>
    <field name="lammitys_tco2" labelOnTop="0"/>
    <field name="liikenne_yht" labelOnTop="0"/>
    <field name="palvliikenne_tco2" labelOnTop="0"/>
    <field name="sahko_kotitaloudet_tco2" labelOnTop="0"/>
    <field name="sahko_palv_tco2" labelOnTop="0"/>
    <field name="sahko_tv_tco2" labelOnTop="0"/>
    <field name="sahko_yht" labelOnTop="0"/>
    <field name="summa" labelOnTop="0"/>
    <field name="tvliikenne_tco2" labelOnTop="0"/>
    <field name="vesi_tco2" labelOnTop="0"/>
    <field name="vuosi" labelOnTop="0"/>
    <field name="xyind" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>fid</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>