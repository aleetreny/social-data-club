"""Additional verified routes and editorial corrections, maintained by hand."""

def extend(institution, program, institutions, programs):
    institution('bundesbank','Deutsche Bundesbank · Research Centre','economia','Alemania','Fráncfort',
        'Banco central alemán con investigación económica, econométrica y microdatos.',
        'Una alternativa al BCE que merece mirar si buscas investigación, no sólo el logo europeo.',
        'Proyectos definidos con economistas y datos; la vía admite máster además de PhD.',
        'Exige matrícula durante la estancia; temas más monetarios y financieros que CSS general.',
        'Compáralo con BCE/BIS por proyecto; puede ser más directo que un graduate generalista.',
        'https://www.bundesbank.de/en/bundesbank/research/research-visit-and-internship')
    program('bundesbank','Research Centre Internships',institutions[-1]['url'],duration='3–6 meses según proyecto',pay='salary',
        eligibility='Estudiantes de máster o PhD, con economía, econometría y matemáticas; matrícula durante toda la estancia.',
        rhythm='Vía de internships por proyectos, sin una fecha universal.',themes='macro,metodos',priority=2,
        fit='Trabajo económico y código con un proyecto concreto. Especialmente útil si tu pregunta social conecta hogares, expectativas o finanzas.',
        watch='La página distingue proyectos del centro y propuestas propias de doctorandos. Los importes generales de prácticas se revalidan con el contrato.')
    institution('dnb','De Nederlandsche Bank','economia','Países Bajos','Ámsterdam',
        'Banco central neerlandés con investigación en macro, banca y econometría.',
        'Potente para el PhD ya en marcha; no lo confundas con una puerta previa al doctorado.',
        'Colaboración investigadora con objetivo de publicación y compensación.',
        'El internship investigador exige una fase avanzada del PhD.',
        'Comparable al fellowship doctoral de BIS y al internship de Bank of England.',
        'https://www.dnb.nl/en/research/phd-internship-programme/phd-internship-program-at-the-de-nederlandsche-bank/')
    program('dnb','PhD Internship Programme',institutions[-1]['url'],stage='phd',duration='3–6 meses',pay='grant',
        eligibility='Doctorandos avanzados en macro, econometría, banca o finanzas; idealmente desde tercer año y cursos terminados.',
        rhythm='Convocatorias del programa; inicio flexible según acuerdo.',themes='macro,metodos',priority=4,
        fit='Investigación conjunta y posible coautoría durante el doctorado.',
        docs='Research statement de hasta 2 páginas, CV y borradores de investigación.',watch='El objetivo de publicación no garantiza un artículo; revalidar convocatoria y compensación.')
    institution('frontier','Frontier Economics','economia','Europa · varias sedes','Oficinas europeas · por puesto',
        'Consultora económica que aplica teoría y análisis a problemas de empresas, mercados y regulación.',
        'Si quieres economía aplicada fuera de la universidad, tiene más sentido que una consultora genérica de datos.',
        'Trabajo económico aplicado y rutas explícitas de interns y analysts.',
        'Trabajo para clientes; confidencialidad y entregables pueden limitar la muestra académica.',
        'Más microeconomía y regulación que un banco central; menos libertad de investigación que una RA.',
        'https://www.frontier-economics.com/uk/en/careers/vacancies-and-apply/')
    program('frontier','Internships',institutions[-1]['url'],pay='unknown',eligibility='Estudiantes de grado en economía en los años indicados o de posgrado económico; verificar oficina.',
        rhythm='Vía de internships de la consultora; condiciones por oficina.',themes='causalidad,metodos',priority=3,
        fit='Entrenamiento aplicado en mercados y policy. Pregunta qué parte será econometría y qué podrás documentar.',watch='Un máster de data science sin suficiente economía puede no encajar.')
    program('frontier','Graduate Analysts',institutions[-1]['url'],kind='canal',pay='salary',eligibility='Máster en economía o economía y finanzas, o grado económico con el nivel requerido.',
        themes='causalidad,metodos',priority=3,fit='Carrera en consultoría económica; útil para métodos y problemas reales, con menos control sobre la pregunta académica.')

    institution('cris','Sciences Po · CRIS','investigacion','Francia','París',
        'Centro de investigación sobre desigualdades sociales, con sociología empírica, educación y demografía.',
        'Muy buena candidata si tu pregunta social manda sobre la herramienta. Hay más vida que los predocs económicos.',
        'Trabajo con encuestas, desigualdad educativa y métodos cuantitativos.',
        'Las prácticas pueden ser de investigación o administrativas; aclara el equipo.',
        'Más sociología y desigualdad que CREI; comparable a WZB o MPIDR según proyecto.',
        'https://www.sciencespo.fr/cris/en/join-us/')
    program('cris','Research Internships',institutions[-1]['url'],kind='canal',pay='unknown',eligibility='La página inglesa contempla grado y máster en sociología; la francesa especifica máster. Confirmar vía y disciplinas.',
        rhythm='Solicitudes motivadas al centro, al menos 4 meses antes según sus páginas.',themes='desigualdad,metodos,salud',priority=1,
        fit='Investigar desigualdad educativa, social o demográfica te da una pregunta sustantiva muy legible para Oxford/LSE.',watch='Pide una asignación investigadora: el centro también admite apoyo administrativo.')
    program('cris','Research Assistant / Predoc · proyectos ERC','https://www.sciencespo.fr/cris/fr/actualites/join-erc-learn-project-team/',kind='canal',pay='unknown',
        eligibility='Ejemplo histórico LEARN: grado o máster en ciencias sociales, métodos básicos, R/Stata e inglés; requisitos por proyecto.',
        rhythm='Contratación por proyectos; el enlace documenta un ejemplo de 2024.',themes='desigualdad,salud,metodos',priority=1,
        fit='Datos, análisis y contribución a artículos: encaje muy directo si el proyecto trata tu tema.',watch='Evidencia histórica de un canal; no un programa predoc anual ni una oferta abierta.')
    institution('medialab','Sciences Po · médialab','investigacion','Francia','París',
        'Laboratorio que cruza ciencias sociales, datos, redes y herramientas digitales.',
        'Una de las alternativas que miraría para plataformas, medios y métodos computacionales.',
        'Preguntas sociales y desarrollo de herramientas de investigación en el mismo entorno.',
        'Research engineer puede exigir experiencia técnica; no asumir un contrato de formación predoc.',
        'Más computacional y digital que CRIS; más cerca del OII por ciertos temas.',
        'https://medialab.sciencespo.fr/en/news/recrute-ingenieure-de-recherche-sur-lecosysteme-mediatique-francais/')
    program('medialab','Research engineering · contratación por proyectos',institutions[-1]['url'],kind='canal',pay='unknown',
        eligibility='Experiencia computacional y perfil según contrato; no se acredita una vía uniforme de recién graduados.',
        rhythm='Por proyecto; fuente histórica identificada como posición cubierta.',themes='plataformas,ia,metodos',priority=2,
        fit='Redes, medios y herramientas de análisis con una pregunta social: excelente puente si puedes contribuir intelectualmente.',watch='El enlace describe un puesto cubierto como evidencia. Mira las noticias del laboratorio para contratación.')
    institution('sodas','Copenhagen Center for Social Data Science · SODAS','investigacion','Dinamarca','Copenhague',
        'Centro interdisciplinar de Social Data Science de la Universidad de Copenhague.',
        'Una referencia europea del cruce social–computacional que conviene tener en el radar.',
        'Integración explícita de métodos computacionales y disciplinas sociales.',
        'Contrata por necesidades; student assistant puede exigir matrícula o tener tareas de apoyo.',
        'Más parecido al OII por el campo que a un internship multilateral por funcionamiento.',
        'https://sodas.ku.dk/dansk/om-centret/')
    program('sodas','Research / student assistants · por proyecto',institutions[-1]['url'],kind='canal',pay='unknown',
        eligibility='Nivel, matrícula e idiomas según puesto; no hay un programa predoc único acreditado aquí.',
        rhythm='Contratación en el portal de la universidad por proyectos.',themes='plataformas,ia,metodos',priority=2,
        fit='Un equipo de Social Data Science con encaje temático puede darte mejores referencias que una institución distante de tu investigación.')
    institution('sofi','Stockholm University · SOFI','investigacion','Suecia','Estocolmo',
        'Instituto de investigación social con proyectos sobre desigualdad, trabajo y educación.',
        'La alternativa nórdica para tomarte la desigualdad social en serio.',
        'Problemas sociales definidos y experiencia con investigación empírica.',
        'Algunos proyectos requieren sueco; contratos de apoyo pueden ser cortos o parciales.',
        'Compáralo con CRIS/WZB por tema, diseño y datos, no sólo por universidad.',
        'https://www.linkedin.com/posts/swedish-institute-for-social-research-sofi_research-assistant-pre-doc-activity-7464613691234115584-4C-Z')
    program('sofi','Research assistants · por proyecto',institutions[-1]['url'],kind='canal',pay='unknown',themes='desigualdad,metodos',priority=2,
        rhythm='Contratos por proyecto; un post de la propia institución documenta un predoc, sin disponibilidad afirmada.',
        fit='Investigar educación, trabajo o desigualdad con un equipo académico. Aclara cuánto análisis harás.',watch='La fuente es un post institucional en LinkedIn y puede pedir acceso. No demuestra un intake predoc único ni requisitos iguales en todos los proyectos.')
    institution('crei','CREI · Centre de Recerca en Economia Internacional','investigacion','España','Barcelona',
        'Instituto de investigación económica en el entorno de UPF y Barcelona School of Economics.',
        'Para economía cuantitativa en España, lo pondría al lado de CEMFI, con foco más macro.',
        'El archivo oficial documenta contratación de RA en varios años.',
        'Los proyectos pueden pedir macro avanzada y Matlab/Stata; CSS no es su única agenda.',
        'Más macro e internacional que J-PAL; buena comparación con CEMFI y los bancos centrales.',
        'https://crei.cat/work-with-us/')
    program('crei','Research Assistants in Economics',institutions[-1]['url'],kind='canal',pay='unknown',
        eligibility='Por proyecto; ejemplos históricos piden máster económico, inglés y programación.',rhythm='Contratación RA documentada en varios años; sin intake común acreditado.',
        themes='macro,metodos',priority=2,fit='Código, simulaciones y datos económicos con investigadores; útil para una candidatura cuantitativa si tu pregunta encaja.')
    institution('bse','Barcelona School of Economics','investigacion','España','Barcelona · Bellaterra',
        'Entorno de investigación y formación económica que contrata asistentes y técnicos para proyectos.',
        'Mira proyecto y afiliación real: BSE es un ecosistema, no un único laboratorio.',
        'Su política de contratación contempla RA y técnicos, con descripciones específicas.',
        'R1 o contrato predoctoral en España puede significar doctorado en curso; leer requisitos.',
        'Se solapa con el entorno de CREI/UPF/UAB, pero no son la misma entidad ni la misma convocatoria.',
        'https://bw.bse.eu/wp-content/uploads/2025/04/bse-hrs4r-otm-r.pdf')
    program('bse','Research Assistants / technicians · por proyecto',institutions[-1]['url'],kind='canal',pay='unknown',themes='causalidad,desigualdad,metodos',priority=2,
        rhythm='Por proyectos; política oficial de selección mediante EURAXESS y otros canales.',fit='Economía empírica con trabajo de datos y supervisión. Revisa la institución contratante y si la vía exige matricularte en un PhD.')
    institution('bit','Behavioural Insights Team · BIT','policy','Global','Londres · oficinas internacionales',
        'Equipo que aplica ciencias del comportamiento y evidencia a decisiones y servicios públicos.',
        'Si quieres evaluar intervenciones, puede encajar mejor que un think tank de opinión.',
        'Orientación empírica y problemas de comportamiento y policy.',
        'Los roles pueden incluir consultoría y gestión; no todos son evaluación causal.',
        'Más intervención aplicada que NatCen; más proyectos de clientes que una RA académica.',
        'https://www.bi.team/about-us/careers/')
    program('bit','Research / evaluation / data · por equipo',institutions[-1]['url'],kind='canal',pay='unknown',themes='causalidad,metodos,desigualdad',priority=2,
        fit='Busca diseño de experimentos, medición y análisis propio. Pregunta qué podrás mostrar de los proyectos de clientes.')
    institution('eth','ETH Zürich · Computational Social Science','investigacion','Suiza','Zúrich',
        'Grupo de investigación computacional sobre sistemas y fenómenos sociales dentro de ETH.',
        'El nombre técnico pesa; comprueba que el rol sea investigación social y no soporte web.',
        'Entorno computacional y proyectos interdisciplinares.',
        'Student assistant también puede significar administración; acceso y nivel varían.',
        'Más sistemas y modelización que CRIS; comparte campo con SODAS, con enfoques distintos.',
        'https://coss.ethz.ch/about/positions.html')
    program('eth','Assistants / research staff · por grupo',institutions[-1]['url'],kind='canal',pay='unknown',themes='plataformas,ia,metodos',priority=2,
        fit='Una pregunta social modelizada con rigor puede aportar mucho. El título de assistant no acredita tareas investigadoras.',watch='Se incluyen puestos de apoyo y el portal ETH. No se promete un predoc uniforme.')

    for args in [
        ('harvard','Harvard · Opportunity Insights','Cambridge, Massachusetts','Centro que estudia movilidad económica y oportunidades con grandes datos administrativos.','Si tu tema es desigualdad, es una de mis primeras paradas fuera de Europa.','Pregunta social central y trabajo empírico intensivo.','Mudanza, requisitos de trabajo y exigencia técnica; confirmar condiciones de cada contratación.','Más movilidad y microdatos que macro; comparable a IFS/J-PAL por investigación aplicada.','https://opportunityinsights.org/team/'),
        ('stanford','Stanford · SIEPR','Stanford, California','Instituto de investigación en política económica con un programa predoc explícito.','Una vía académica seria para economía, policy y campos cercanos.','Trabajo con uno o dos faculty y desarrollo cuantitativo; posibilidad de cursos.','Coste de vida, visado y asignación concreta; no confundir el nombre con garantía de supervisión.','Comparable a Tobin/BFI por estructura predoc, con investigadores y temas distintos.','https://siepr.stanford.edu/programs/siepr-predoctoral-research-fellows-program'),
        ('chicago','Chicago · Becker Friedman Institute','Chicago','Instituto de investigación económica con formación predoc y trabajo con faculty.','Potente si tu PhD necesita economía empírica y rigor cuantitativo.','Programa que combina investigación, seminarios, cursos y mentoría.','Predomina economía; publicaciones y destinos de antiguos participantes no son probabilidades.','Comparable a LSE/IFS por experiencia económica y a SIEPR/Tobin por estructura estadounidense.','https://bfi.uchicago.edu/info-for/prep/'),
        ('yale','Yale · Tobin Center','New Haven, Connecticut','Centro de policy económica con un programa predoc para investigación social intensiva en datos.','Buena alternativa para construir una candidatura con trabajo académico concreto.','Uno o más mentores, comunidad, formación y posibilidad de cursos.','Trabajo presencial y compromiso largo; exigencias específicas por proyecto.','Comparable a SIEPR/BFI; decide por mentor, método y problema, no por la camiseta universitaria.','https://tobin.yale.edu/programs/pre-doctoral-fellows-program/apply'),
        ('mit','MIT · Blueprint Labs','Cambridge, Massachusetts','Laboratorio que usa economía y datos para educación, salud y trabajo.','Para IA, trabajo y evaluación de políticas, tiene un encaje especialmente bueno.','Predoc con gestión de código, análisis, escritura y apoyo de una cohorte.','La descripción consultada no ofrece sponsorship de visado; tener derecho a trabajar es decisivo.','Más evaluación y economía aplicada que ML industrial; J-PAL y Blueprint son vías diferentes aunque compartan entorno MIT.','https://blueprintlabs.mit.edu/careers/'),
        ('princeton','Princeton · Economics research groups','Princeton, New Jersey','Departamento con unidades de trabajo, finanzas públicas, desarrollo y economía internacional.','Una familia de vías predoc; mira la unidad que investiga tu tema.','El departamento documenta unidades que contratan RA/predocs de forma habitual.','No hay un contrato uniforme para todo Princeton; grado local y predoc externo son vías distintas.','Comparable a otros predocs económicos por equipo; Industrial Relations puede encajar más que una unidad macro.','https://economics.princeton.edu/undergraduate-program/funding-research-assistant-and-career-opportunities/')]:
        id,name,city,intro,verdict,up,down,comparison,url=args
        institution(id,name,'investigacion','Estados Unidos',city,intro,verdict,up,down,comparison,url)
    program('harvard','Predoctoral Fellowship','https://opportunityinsights.org/wp-content/uploads/2022/09/OI_Predoc_Fall2022_Flyer.pdf',pay='unknown',
        eligibility='Perfil cuantitativo y requisitos de la contratación; el documento enlazado es histórico.',rhythm='Fellowship documentado y cohorte de predocs en la página del equipo.',
        themes='desigualdad,causalidad,metodos',priority=1,fit='Movilidad y desigualdad con datos a escala: encaje muy directo con una propuesta social cuantitativa.',watch='La convocatoria PDF es de 2022; sirve para documentar la vía, no las condiciones ni disponibilidad de una edición actual.')
    program('stanford','Predoctoral Research Fellows Program','https://siepr.stanford.edu/programs/siepr-predoctoral-research-fellows-program',pay='unknown',
        eligibility='Grado/máster completado o en último año; capacidades y requisitos del proyecto.',rhythm='Programa con fellows y contratación por proyectos.',
        themes='desigualdad,causalidad,ia',priority=1,fit='Trabajo a tiempo completo con faculty, formación cuantitativa y conocimiento del proceso investigador: vía diseñada para preparar el PhD.')
    program('chicago','Predoctoral Research in Economics Program · PREP','https://bfi.uchicago.edu/info-for/prep/',pay='unknown',
        eligibility='Perfil para investigación económica empírica; requisitos de cada puesto.',rhythm='Ciclos de contratación de otoño, invierno y primavera según página.',
        themes='causalidad,desigualdad,macro',priority=1,fit='RA con faculty, orientación, mentoría y formación: una experiencia sostenida para aprender economía empírica.',watch='Los destinos publicados son ejemplos de antiguos participantes, no una tasa de admisión ni un efecto causal del programa.')
    program('yale','Tobin / Economics Pre-Doctoral Fellows Program','https://tobin.yale.edu/programs/pre-doctoral-fellows-program/apply',duration='1–2 años',pay='unknown',
        eligibility='Grado o máster y habilidades pertinentes al proyecto; trabajo a tiempo completo en el campus.',rhythm='Cohortes y aplicación común con preferencias por proyectos.',
        themes='causalidad,desigualdad,ia',priority=1,fit='Investigación social intensiva en datos y supervisión de faculty: buen material para propuesta, escritura y referencias.',docs='Aplicación común, CV, motivación, expediente y referencias; revisar lista completa en la fuente.')
    program('mit','Predoctoral Researchers','https://blueprintlabs.mit.edu/careers/predoctoral-researcher/',duration='1 año · renovación por acuerdo y financiación',pay='salary',
        eligibility='Perfil cuantitativo relevante, sin PhD; no exige major en economía. Derecho a trabajar en EEUU, sin sponsorship según descripción.',
        rhythm='Vía predoc recurrente con contratación de cohortes/proyectos.',themes='causalidad,ia,desigualdad,salud',priority=1,
        fit='Educación, trabajo, salud y econometría con código y escritura. Muy pertinente si investigas los efectos sociales de la tecnología.',watch='Revalidar derecho a trabajar, renovación y proyecto. La página concreta manda sobre condiciones futuras.',docs='CV, motivación y muestra escrita; proceso con entrevistas y tareas según el laboratorio.')
    program('princeton','Research assistants / predocs · por unidad','https://economics.princeton.edu/join-our-team/',kind='canal',pay='unknown',
        eligibility='Grado y capacidades según unidad/contrato; diferenciar puestos internos de grado.',rhythm='Unidades con contratación habitual, a menudo en otoño según página del departamento.',
        themes='desigualdad,causalidad,macro',priority=1,fit='Investigación con economistas por unidad; elige trabajo, desarrollo o policy si buscas un puente a CSS.')

    portals = {
        'oxford':'https://www.oii.ox.ac.uk/people/vacancies/',
        'bocconi':'https://careers.unibocconi.it/',
        'natcen':'https://natcen.ac.uk/work-for-us',
        'sodas':'https://employment.ku.dk/all-vacancies/',
        'bse':'https://bse.eu/research/job-openings',
        'harvard':'https://opportunityinsights.org/joinourteam/',
        'princeton':'https://economics.princeton.edu/join-our-team/',
        'bundesbank':'https://www.bundesbank.de/en/career/opportunities/work-placements-for-university-students-616360',
        'medialab':'https://medialab.sciencespo.fr/en/news/',
        'sofi':'https://www.su.se/vacancies',
    }
    for i in institutions:
        if i['id'] in portals: i['portal']=portals[i['id']]
        if i['id']=='dfki': i['url']='https://dsa.dfki.de/for-students/'
        if i['id']=='natcen': i['url']=portals['natcen']
        if i['id'] in ['boe','bdf']: i['group']='economia'
    for p in programs:
        i=next(i for i in institutions if i['id']==p['institution'])
        p['group']=i['group']
        if p['institution'] in portals: p['portal']=portals[p['institution']]
        if p['institution']=='dfki':p['url']='https://dsa.dfki.de/for-students/'
        if p['institution']=='nato' and 'Young' in p['name']:
            p['url']='https://www.nato.int/en/work-with-us/careers/young-professionals--programme'
            p['eligibility']='21–32 años, ciudadanía de país aliado, máster, al menos un año de experiencia e inglés o francés; requisitos de la edición.'
        if p['institution']=='eea':
            p.update(kind='destino',name='Blue Book · destino EEA',duration='Según asignación Blue Book',pay='grant',
                eligibility='Elegibilidad del Blue Book y perfil de la asignación en EEA.',
                rhythm='La agencia participa en el esquema Blue Book; revisar asignaciones.',
                fit='Evidencia ambiental y policy europea; busca un proyecto con dimensión social o territorial.',
                watch='EEA es un destino del Blue Book, no un programa separado. No sumar ambas fichas como dos vías de acceso distintas.')
        if p['institution']=='ms' and 'Cambridge' in p['name']:p['country']='Reino Unido'
        if p['institution']=='ms' and 'Predoctoral' in p['name']:p['country']='Estados Unidos'
        if p['fit'].startswith('Elige un proyecto con análisis propio'):
            p['fit']=i['verdict']+' '+i['comparison']
