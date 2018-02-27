Shader "Toon" {
  Properties {
    _ToonColor ("Toon Color", Color) = (1,1,1,1)
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
          half toon = 1.0;

          // TODO: update toon to implement toon shading

          return toon * _ToonColor;
      }
      ENDCG
    }
  }
}
