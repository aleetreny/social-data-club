# Social Data Club

Un atlas estático en español para orientarse entre instituciones, programas recurrentes y contratación de investigación relevantes para Social Data Science. La orientación editorial prioriza preparar una candidatura al **Oxford DPhil in Social Data Science** o al **LSE MPhil/PhD Computational Social Science**.

**Web:** https://aleetreny.github.io/social-data-club/

La edición del 30 de septiembre de 2026 contiene **112 instituciones, 142 rutas y 161 referencias enlazadas**. Se distinguen 97 programas documentados, 44 canales de contratación por equipos y un destino de otro programa. EEA participa mediante Blue Book: sus dos fichas no representan dos mecanismos independientes de acceso.

## Qué puedes hacer

- Entender siete familias de instituciones y sus diferencias, con una lectura editorial directa.
- Buscar por palabras y filtrar por familia, tema, país/ámbito, etapa y condiciones económicas.
- Consultar fichas con requisitos, duración, recurrencia, documentación, límites y fuentes.
- Comparar hasta tres rutas por condiciones y encaje investigador.
- Leer experiencias públicas distinguiendo reseñas independientes, foros y testimonios institucionales.
- Descargar la bibliografía y consultar los portales oficiales por tu cuenta.

## Una edición estática

No es una bolsa de empleo. No muestra puestos abiertos ni próximos cierres. No tiene backend, feeds de vacantes, scraping periódico ni tareas programadas para actualizar disponibilidad. El único workflow publica cambios del repositorio en GitHub Pages; no investiga ni actualiza las convocatorias.

La recurrencia describe un esquema institucional o un historial documentado, sin prometer una edición futura. Las prioridades son juicios editoriales, no rankings oficiales, tasas de admisión ni evidencia de que una experiencia cause la entrada en un doctorado. Los requisitos deben contrastarse con la convocatoria correspondiente.

Europa es el centro del mapa; se incluyen organismos globales y predocs especialmente pertinentes fuera de Europa. La cobertura es amplia, pero no es un censo de todas las empresas, universidades o programas existentes. Véase [el alcance de la investigación](research/METODOLOGIA.md).

## Ejecutar y editar

Requiere Python 3 para regenerar el catálogo; la web publicada sólo necesita HTML, CSS y JavaScript.

```sh
python3 scripts/build_catalogue.py
python3 scripts/validate.py
python3 -m http.server 8765 --directory dist
```

Abrir http://127.0.0.1:8765/. Los datos editoriales se mantienen a mano en `scripts/build_catalogue.py` y `scripts/expand_catalogue.py`; la generación produce `data/catalogue.json`, `dist/catalogue.js` y `dist/fuentes.txt`.

`scripts/check_links.py` es una comprobación manual de enlaces, sin temporizador ni conexión con la web. Un HTTP 403/429 o bloqueo de robots no permite concluir que una vía haya desaparecido. Los resultados brutos locales de investigación no forman parte de la publicación.

## Publicación

GitHub Pages publica sólo `dist/`. El workflow valida los datos y la sintaxis, regenera el catálogo y añade `build-info.json` con el commit desplegado. Los enlaces de recursos son relativos para funcionar bajo `/social-data-club/`. La navegación por fragmentos permite compartir fichas y filtros sin necesitar un servidor de rutas.

La estética toma como referencia el verde, coral, papel, tipografía condensada y bordes marcados de Hacktoberfest, con identidad y composición propias. Las tipografías se sirven mediante Google Fonts, con alternativas del sistema. Los textos son síntesis editoriales originales; los documentos enlazados y marcas de terceros conservan sus derechos.
