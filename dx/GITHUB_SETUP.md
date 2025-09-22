# 🚀 Comandos para subir a GitHub

## 1. Crear repositorio en GitHub.com
- Ve a: https://github.com/new
- Nombre: `team-skills-radar`
- Descripción: `🎯 Generador de radares de habilidades visuales para equipos - SVG con efectos premium`
- Público ✅
- **NO** inicializar con README

## 2. Conectar y subir
```bash
git remote add origin https://github.com/Seir/team-skills-radar.git
git branch -M main
git push -u origin main
```

## 3. Verificar
- Deberías ver todos los archivos en GitHub
- 13 SVGs en la carpeta `output/`
- README.md con documentación
- Estadísticas completas en `docs/`

## 📋 Checklist final
- ✅ Repositorio Git local listo
- ✅ Documentación simplificada
- ✅ Estructura organizada
- ⏳ Crear repo en GitHub
- ⏳ Push inicial

## 🔧 Si hay problemas de autenticación
```bash
# Usar token personal en lugar de contraseña
git remote set-url origin https://TOKEN@github.com/USERNAME/team-skills-radar.git
```

Obtén tu token en: https://github.com/settings/tokens