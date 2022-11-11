vertex_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;
    pos = (modelMatrix * vec4(position + normals * sin(time * 3)/10, 1.0)).xyz;

    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(position, 1.0);

}
'''


fragment_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));

    fragColor = texture(tex, UVs) * intensity;
}
'''

toon_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    if (intensity < 0.2){
        intensity = 0.1;
    } else if (intensity < 0.5){
        intensity = 0.4;
    } else if (intensity < 0.7){
        intensity = 0.6;
    } else if (intensity < 0.9){
        intensity = 0.8;
    } else if (intensity < 0.94){
        intensity = 0.9;
    } else {
        intensity = 1;
    }
    fragColor = texture(tex, UVs) * intensity;
}
'''

rainbow_shader ='''
#version 450 core

out vec4 fragColor;

in vec2 UVs;
in vec3 norms;
in vec3 pos;

uniform vec3 pointLight;

uniform sampler2D tex;

void main()
{
    float intensity = dot(norms, normalize(pointLight - pos));
    if (intensity < 0.2){
        fragColor = texture(tex, UVs) *  vec4(0.3,0.5,0.8,1.0);
    } else if (intensity < 0.5){
      fragColor = texture(tex, UVs) *  vec4(0.6,0.9,0.1,1.0);
    } else if (intensity < 0.7){
       fragColor = texture(tex, UVs) *  vec4(0.9,0.2,0.4,1.0);
    } else if (intensity < 0.9){
       fragColor = texture(tex, UVs) *  vec4(0.2,0.6,0.8,1.0);
    } else if (intensity < 0.94){
       fragColor = texture(tex, UVs) *  vec4(0.5,0.3,0.3,1.0);
    } else {
       fragColor = texture(tex, UVs) *  vec4(0,0,0,1.0);
    }
}
'''

deform_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;

    pos = (modelMatrix * vec4( position + normals, 1.0)).xyz;
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4( normals/10 + position, 1.0);
}
'''

sphere_shader ='''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texcoords;
layout (location = 2) in vec3 normals;

uniform mat4 modelMatrix;
uniform mat4 viewMatrix;
uniform mat4 projectionMatrix;

uniform float time;

out vec2 UVs;
out vec3 norms;
out vec3 pos;

void main()
{
    UVs = texcoords;
    norms = normals;

    pos = (modelMatrix * vec4( position + normals, 1.0)).xyz;
    gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4( normals + position/10, 1.0);
}
'''