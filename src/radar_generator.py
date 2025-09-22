import math

def generate_custom_radar(mathematics=8, programming=7, teamwork=6, discipline=5, sociability=9, 
                         filename="mi_radar_personalizado.svg", name=""):
    """
    Genera un radar chart personalizado con tus propios valores de habilidades
    (parcheado: filtros en userSpaceOnUse para evitar clipping de la línea vertical MATHEMATICS).
    """
    values = [mathematics, programming, teamwork, discipline, sociability]
    labels = ["MATHEMATICS", "PROGRAMMING", "TEAMWORK", "DISCIPLINE", "SOCIABILITY"]
    # Clamp values 0-10
    values = [max(0, min(10, v)) for v in values]
    
    # Configuración
    width, height = 700, 700
    center_x, center_y = width // 2, height // 2
    max_radius = 220
    
    # Calcular ángulos (MATHEMATICS hacia arriba)
    n = len(labels)
    angles = [(2 * math.pi * i) / n - math.pi/2 for i in range(n)]
    
    # Dimensiones seguras para filtros en coordenadas absolutas del canvas
    fx, fy, fw, fh = -150, -150, width + 300, height + 300
    
    # Generar SVG
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="bgGrad" cx="50%" cy="50%">
      <stop offset="0%" style="stop-color:#2c5aa0;stop-opacity:1" />
      <stop offset="70%" style="stop-color:#1a365d;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0f1419;stop-opacity:1" />
    </radialGradient>
    
    <!-- PARCHE: usar coordenadas absolutas para evitar bbox degeneradas -->
    <filter id="strongGlow" filterUnits="userSpaceOnUse"
            x="{fx}" y="{fy}" width="{fw}" height="{fh}">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge> 
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <filter id="softGlow" filterUnits="userSpaceOnUse"
            x="{fx}" y="{fy}" width="{fw}" height="{fh}">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge> 
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <filter id="redAreaBlur" filterUnits="userSpaceOnUse"
            x="{fx}" y="{fy}" width="{fw}" height="{fh}">
      <feGaussianBlur stdDeviation="1.5" result="coloredBlur"/>
      <feMerge> 
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    
    <!-- Filtro para sombra interior -->
    <filter id="innerShadow" filterUnits="userSpaceOnUse"
            x="{fx}" y="{fy}" width="{fw}" height="{fh}">
      <feGaussianBlur stdDeviation="3"/>
      <feOffset dx="2" dy="2" result="offset"/>
      <feComposite in="SourceGraphic" in2="offset" operator="out"/>
    </filter>
    
    <!-- Gradiente para el área de datos -->
    <radialGradient id="dataGrad" cx="50%" cy="30%">
      <stop offset="0%" style="stop-color:#FF6B6B;stop-opacity:0.9" />
      <stop offset="70%" style="stop-color:#D32F2F;stop-opacity:0.8" />
      <stop offset="100%" style="stop-color:#B71C1C;stop-opacity:0.6" />
    </radialGradient>
    
    <pattern id="techGrid" width="15" height="15" patternUnits="userSpaceOnUse">
      <path d="M 15 0 L 0 0 0 15" fill="none" stroke="#4FC3F7" stroke-width="0.3" opacity="0.4"/>
      <circle cx="0" cy="0" r="0.5" fill="#4FC3F7" opacity="0.6"/>
    </pattern>
  </defs>
  
  <rect width="{width}" height="{height}" fill="url(#bgGrad)"/>
  <rect width="{width}" height="{height}" fill="url(#techGrid)"/>'''
    
    # Pentágonos concéntricos
    for level in [2, 4, 6, 8, 10]:
        radius = (level / 10) * max_radius
        opacity = 0.8 if level == 10 else 0.6
        
        pentagon_points = []
        for angle in angles:
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            pentagon_points.append(f"{round(x, 1)},{round(y, 1)}")
        
        pentagon_points_str = " ".join(pentagon_points)
        svg_content += f'''
  <polygon points="{pentagon_points_str}" 
           fill="none" stroke="#64B5F6" stroke-width="1.5" 
           opacity="{opacity}" filter="url(#softGlow)"/>'''
    
    # Polígono de datos
    points = []
    for value, angle in zip(values, angles):
        radius = (value / 10) * max_radius
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        points.append(f"{round(x, 1)},{round(y, 1)}")
    points.append(points[0])
    points_str = " ".join(points)
    
    svg_content += f'''
  <polygon points="{points_str}" 
           fill="url(#dataGrad)" 
           stroke="#F44336" stroke-width="3" 
           filter="url(#redAreaBlur)"/>'''
    
    # Líneas radiales
    for label, angle in zip(labels, angles):
        end_x = center_x + max_radius * math.cos(angle)
        end_y = center_y + max_radius * math.sin(angle)
        stroke_width = "4" if label == "MATHEMATICS" else "3"
        stroke_color = "#FFFFFF" if label == "MATHEMATICS" else "#E1F5FE"
        svg_content += f'''
  <line x1="{center_x}" y1="{center_y}" x2="{end_x}" y2="{end_y}" 
        stroke="{stroke_color}" stroke-width="{stroke_width}" stroke-linecap="round"
        filter="url(#strongGlow)"/>'''
    
    # Puntos en vértices con efecto de pulso
    for i, (value, angle) in enumerate(zip(values, angles)):
        radius = (value / 10) * max_radius
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # Círculo base con gradiente
        svg_content += f'''
  <circle cx="{x}" cy="{y}" r="6" 
          fill="url(#dataGrad)" stroke="#FFFFFF" stroke-width="2" 
          filter="url(#strongGlow)">
    <animate attributeName="r" values="6;8;6" dur="2s" repeatCount="indefinite" 
             begin="{i * 0.4}s"/>
  </circle>
  <!-- Círculo interior brillante -->
  <circle cx="{x}" cy="{y}" r="3" 
          fill="#FFFFFF" opacity="0.8"/>'''
    
    # Etiquetas
    for label, value, angle in zip(labels, values, angles):
        label_distance = max_radius + 50
        label_x = center_x + label_distance * math.cos(angle)
        label_y = center_y + label_distance * math.sin(angle) + 6
        
        svg_content += f'''
  <text x="{label_x}" y="{label_y}" 
        fill="#FFFFFF" font-family="Arial Black, Arial" font-size="16" font-weight="bold" 
        text-anchor="middle" filter="url(#softGlow)">{label}</text>
  <text x="{label_x}" y="{label_y + 20}" 
        fill="#4FC3F7" font-family="Arial" font-size="12" font-weight="bold" 
        text-anchor="middle">({value})</text>'''
    
    # Agregar nombre del integrante si se proporciona
    if name:
        svg_content += f'''
  <text x="{center_x}" y="40" 
        fill="#FFFFFF" font-family="Arial Black, Arial" font-size="24" font-weight="bold" 
        text-anchor="middle" filter="url(#strongGlow)">{name}</text>
  <text x="{center_x}" y="65" 
        fill="#4FC3F7" font-family="Arial" font-size="14" font-weight="bold" 
        text-anchor="middle">SKILLS RADAR</text>'''
    
    # Centro con efecto pulsante
    svg_content += f'''
  <circle cx="{center_x}" cy="{center_y}" r="8" 
          fill="#4FC3F7" stroke="#FFFFFF" stroke-width="3" 
          filter="url(#strongGlow)">
    <animate attributeName="fill-opacity" values="0.8;1;0.8" dur="3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="{center_x}" cy="{center_y}" r="4" 
          fill="#FFFFFF" opacity="0.9"/>
</svg>'''
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)
    return filename

def generate_team_radars():
    """
    Genera radares SVG para todos los integrantes del equipo
    NOTA: Actualiza los datos según la información del PDF stats.pdf
    """
    # Datos actualizados del equipo completo
    team_members = [
        {
            "name": "CHAFITA",
            "discipline": 6.62,
            "mathematics": 6.38,
            "programming": 6.25,
            "sociability": 8.88,
            "teamwork": 5.12
        },
        {
            "name": "CHAY",
            "discipline": 3.56,
            "mathematics": 4.56,
            "programming": 4.11,
            "sociability": 7.67,
            "teamwork": 5.56
        },
        {
            "name": "EDREI",
            "discipline": 3.78,
            "mathematics": 3.89,
            "programming": 3.56,
            "sociability": 4.33,
            "teamwork": 3.89
        },
        {
            "name": "ESTEBAN",
            "discipline": 6.75,
            "mathematics": 6.12,
            "programming": 6.25,
            "sociability": 5.50,
            "teamwork": 6.75
        },
        {
            "name": "HERBERT",
            "discipline": 6.00,
            "mathematics": 5.88,
            "programming": 6.50,
            "sociability": 7.75,
            "teamwork": 7.12
        },
        {
            "name": "ISAAC",
            "discipline": 6.38,
            "mathematics": 5.25,
            "programming": 8.50,
            "sociability": 6.50,
            "teamwork": 9.50
        },
        {
            "name": "JESUS CRUZ",
            "discipline": 7.33,
            "mathematics": 7.22,
            "programming": 7.33,
            "sociability": 7.66,
            "teamwork": 7.00
        },
        {
            "name": "NICO",
            "discipline": 4.62,
            "mathematics": 3.25,
            "programming": 4.12,
            "sociability": 7.88,
            "teamwork": 6.75
        },
        {
            "name": "RAMON",
            "discipline": 5.89,
            "mathematics": 6.78,
            "programming": 5.89,
            "sociability": 4.78,
            "teamwork": 6.22
        },
        {
            "name": "RICHARD",
            "discipline": 7.25,
            "mathematics": 7.25,
            "programming": 9.62,
            "sociability": 4.62,
            "teamwork": 8.12
        },
        {
            "name": "SAID",
            "discipline": 8.12,
            "mathematics": 9.12,
            "programming": 8.00,
            "sociability": 6.50,
            "teamwork": 8.50
        },
        {
            "name": "SERGIO",
            "discipline": 8.12,
            "mathematics": 8.00,
            "programming": 6.12,
            "sociability": 5.12,
            "teamwork": 7.50
        },
        {
            "name": "VALERIA",
            "discipline": 9.25,
            "mathematics": 9.25,
            "programming": 6.38,
            "sociability": 7.75,
            "teamwork": 7.50
        }
    ]
    
    generated_files = []
    
    for member in team_members:
        filename = f"radar_{member['name'].lower().replace(' ', '_')}.svg"
        archivo = generate_custom_radar(
            mathematics=member['mathematics'],
            programming=member['programming'],
            teamwork=member['teamwork'],
            discipline=member['discipline'],
            sociability=member['sociability'],
            filename=filename,
            name=member['name']
        )
        generated_files.append(archivo)
        print(f"✅ Radar generado para {member['name']}: {archivo}")
    
    return generated_files

# Ejecutar la función para generar el radar
if __name__ == "__main__":
    print("🎯 Generando radares para todo el equipo...")
    print("📋 NOTA: Actualiza los datos en generate_team_radars() con la info del PDF stats.pdf")
    print("-" * 60)
    
    # Generar radares para todos los integrantes
    archivos_generados = generate_team_radars()
    
    print("-" * 60)
    print(f"🎉 ¡Completado! Se generaron {len(archivos_generados)} radares:")
    for archivo in archivos_generados:
        print(f"   📊 {archivo}")
    
    print("\n💡 Para personalizar: modifica los datos en la función generate_team_radars()")
    
    # También puedes generar uno individual así:
    # archivo_individual = generate_custom_radar(mathematics=9, programming=8, teamwork=7, discipline=6, sociability=10, filename="mi_radar_personal.svg", name="TU NOMBRE")
    # print(f"Radar individual generado: {archivo_individual}")
