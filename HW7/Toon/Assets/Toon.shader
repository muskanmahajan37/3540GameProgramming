Shader "Toon" {
  Properties {
    _ToonColor ("Toon Color", Color) = (1,0,0,1)
  }

  SubShader {
    Tags {
      "LightMode"="ForwardBase"
      "Queue"="Geometry"
      "RenderType"="Opaque"
    }

    Pass {
      CGPROGRAM
      #pragma vertex vert
      #pragma fragment frag
      #include "UnityCG.cginc"
      
      struct vertInput {
        float4 pos : POSITION;
        float3 normal : NORMAL;
      };

      struct vertOutput {
        float4 pos : SV_POSITION;
        float3 normal : TEXCOORD0;
      };

      vertOutput vert(vertInput input) {
        vertOutput o;
        o.pos = UnityObjectToClipPos(input.pos);
        o.normal = UnityObjectToWorldNormal(input.normal);
        return o;
      }

      half4 _ToonColor;

      half4 frag(vertOutput output) : COLOR {
          // TODO: update toon to implement toon shading
		  half toonLight = 1.0;
		  half toonMed = 0.5;
		  half toonDark = 0.3;

		  half dotResult = dot (output.pos, output.normal);

		  if (dotResult < -150) {
			  return toonDark * _ToonColor;
		  }
		  else if (dotResult < 50) {
			  return toonMed * _ToonColor;
		  }

          return toonLight * _ToonColor;
      }
      ENDCG
    }
  }
}
