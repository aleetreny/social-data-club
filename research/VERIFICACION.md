# Verificación de la edición

El catálogo se validó con 112 instituciones, 142 rutas, referencias cruzadas coherentes, identificadores únicos y fuentes con URL válida. La generación es reproducible desde los dos scripts editoriales y la web no consulta ofertas.

La comprobación manual de enlaces alcanzó las 163 referencias: 123 devolvieron HTTP 200 y ninguna HTTP 404. El resto incluye bloqueos de automatización, respuestas 403/429, una respuesta 202 y errores TLS; no se presentan como acceso íntegro verificado. Se consultaron también resultados y páginas oficiales para las vías correspondientes. Los enlaces de contratación añadidos se comprobaron por separado.

Se probaron en el navegador:

- Búsqueda, limpieza, filtros de familia/país/etapa y estados sin resultados.
- Distinción entre programas, destinos y contratación por equipos.
- Comparación de OCDE, MPIDR y LSE; límite de tres selecciones.
- Fichas de programas e instituciones, cierre con Escape y retorno del foco.
- Clasificación de familias y las ocho entradas de voces con sus fuentes.
- Diseño en pantalla estrecha, sin desbordamiento horizontal del documento; la tabla conserva desplazamiento propio.

GitHub Actions valida los datos y la sintaxis antes de desplegar. La versión pública se contrasta con `build-info.json`, que identifica el commit publicado. Este documento describe las comprobaciones de esta edición; no es un monitor ni implica comprobaciones periódicas.
