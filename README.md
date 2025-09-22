# 🎯 Team Skills Radar Generator

Genera radares de habilidades visuales para equipos. Crea gráficos SVG profesionales con efectos visuales que muestran las competencias de cada miembro.

## ✨ Características

- 📊 **5 habilidades**: Matemáticas, Programación, Teamwork, Disciplina, Sociabilidad
- � **Efectos visuales**: Blur, gradientes, animaciones
- 👥 **Generación masiva** para equipos completos
- � **Formato SVG** escalable y profesional

## 📂 Estructura del Proyecto

```
├── src/
│   └── radar_generator.py    # Código principal del generador
├── output/
│   ├── radar_chafita.svg     # Radares generados para cada miembro
│   ├── radar_chay.svg
│   └── ...                   # 13 radares en total
├── docs/
│   └── team_stats.md         # Documentación de estadísticas
└── README.md                 # Este archivo
```

## 🚀 Uso

```bash
git clone https://github.com/Seir/team-skills-radar.git
cd team-skills-radar
python src/radar_generator.py
```

Los archivos SVG se generan en la carpeta `output/`.

## 📊 Equipo Actual

13 integrantes con evaluación en escala 0-10:
- **Top Matemáticas**: Valeria (9.25), Said (9.12)
- **Top Programación**: Richard (9.62), Isaac (8.50)  
- **Top Teamwork**: Isaac (9.50), Richard (8.12)
- **Top Disciplina**: Valeria (9.25), Said (8.12)
- **Top Sociabilidad**: Chafita (8.88), Nico (7.88)

Ver análisis interactivo:
- **GitHub Pages**: [Dashboard Interactivo](https://seir.github.io/team-skills-radar/docs/team_stats.html)
- **Vista Previa**: [HTMLPreview](https://htmlpreview.github.io/?https://github.com/Seir/team-skills-radar/blob/main/docs/team_stats.html)

## 🎨 Personalización

Edita `team_members` en `src/radar_generator.py`:

```python
{
    "name": "NOMBRE",
    "discipline": 8.5,
    "mathematics": 7.2, 
    "programming": 9.1,
    "sociability": 6.8,
    "teamwork": 8.0
}
```

## � Licencia

MIT License - ver [`LICENSE`](LICENSE)
