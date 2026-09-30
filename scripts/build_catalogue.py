"""Editorial snapshot. Only manually run: no feeds, schedules, vacancy fetching."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
institutions, programs = [], []

def institution(id, name, group, country, city, intro, verdict, upside, downside, comparison, url):
    institutions.append(dict(id=id, name=name, group=group, country=country, city=city,
        intro=intro, verdict=verdict, upside=upside, downside=downside, comparison=comparison, url=url))

def program(inst, name, url, stage='pre', kind='programa', duration='Según convocatoria', pay='unknown',
            eligibility='Requisitos específicos del equipo y de la convocatoria.', rhythm='Por equipo, sin calendario único.',
            themes='metodos', priority=3, fit='Elige un proyecto con análisis propio, supervisión y un resultado que puedas enseñar.',
            watch='Confirma equipo, tareas, supervisión, permisos para publicar y elegibilidad en la fuente oficial.',
            docs='CV, motivación y documentación académica; requisitos finales en el portal.', location=None):
    i=next(x for x in institutions if x['id']==inst)
    pid=inst+'-'+str(1+sum(x['institution']==inst for x in programs))
    programs.append(dict(id=pid,institution=inst,name=name,url=url,stage=stage,kind=kind,duration=duration,pay=pay,
        eligibility=eligibility,rhythm=rhythm,themes=themes.split(','),priority=priority,fit=fit,watch=watch,docs=docs,
        location=location or i['city'],country=i['country'],group=i['group'],reviewed='2026-09-30'))

institution('oecd','OCDE / OECD','multilateral','Francia','París · modalidad por equipo',
'El club de países que compara educación, empleo, desigualdad y políticas públicas con datos. Sus informes acaban en los despachos de gobiernos.',
'Mi primera apuesta multilateral si tu tema es IA, trabajo, habilidades o política digital.',
'Datos comparables entre países y preguntas sociales reconocibles para una tesis.',
'La práctica puede ser análisis o apoyo administrativo. París y el estipendio importan.',
'Más transversal que el FMI; menos trabajo de campo que J-PAL. Para tu tema, elegiría STI, ELS, GOV, EDU o estadística.',
'https://www.oecd.org/en/about/careers/internships.html')
program('oecd','Internship Programme','https://www.oecd.org/en/about/careers/internships.html',duration='1–6 meses · hasta 12 con renovación',pay='grant',eligibility='Matrícula a tiempo completo durante toda la práctica; inglés o francés y disposición a aprender el otro. Prioridad a nacionales de países miembros.',rhythm='Solicitudes durante el año; asignación según equipos.',themes='ia,desigualdad,metodos',priority=1,fit='Muy buen encaje si produces un análisis reproducible sobre empleo, educación, IA o desigualdad.',watch='La modalidad remota depende del equipo; no implica permiso para trabajar desde Reino Unido. Normalmente 40 h; parcial excepcional desde 20 h.')
program('oecd','Young Associates Programme','https://www.oecd.org/en/about/careers/young-associates.html',stage='grado',duration='2 años',pay='salary',eligibility='Graduados recientes de grado. No admite a quienes ya cursan o tienen máster; nacionalidad y cohorte según reglas.',rhythm='Cohortes; puede haber aplazamientos.',themes='ia,desigualdad',priority=4,fit='Está diseñado como preparación de posgrado, pero tu etapa de formación ya supera la elegibilidad.',watch='Con máster, mira Internship Programme o contratación profesional. No tratar una cohorte futura como garantizada.')

institution('worldbank','Banco Mundial / World Bank Group','multilateral','Global','Washington DC · oficinas de país',
'Un grupo de instituciones que financia desarrollo y produce investigación sobre pobreza, servicios y crecimiento. DIME es la parte que pone evaluaciones de impacto a trabajar.',
'Si el destino es DIME o investigación de desarrollo, está en mi primera línea.',
'Problemas sociales, datos de programas y contacto con investigadores.',
'Una práctica corporativa no tiene la misma utilidad que una evaluación de impacto.',
'Más ligado a proyectos de desarrollo que la OCDE. DIME compite con J-PAL por encaje investigador; el nombre del banco solo no decide.',
'https://www.worldbank.org/ext/en/careers/talent-programs/wbg-pioneers')
program('worldbank','WBG Pioneers','https://www.worldbank.org/ext/en/careers/talent-programs/wbg-pioneers',duration='Según asignación',pay='varies',eligibility='Último año de grado o matrícula de máster/PhD; ciudadanía de país miembro; experiencia dentro del rango del programa.',rhythm='Ciclos de prácticas; consultar patrón y edición en el portal.',themes='causalidad,desigualdad,metodos',priority=1,fit='Priorizar Development Impact / DIME, economía del desarrollo y datos. Una evaluación o trabajo de reproducibilidad conecta muy bien con el PhD.',watch='La página describe prácticas pagadas y contempla casos sin pago: comprobar contrato concreto. Lugar y trabajo remoto dependen de la asignación.')
program('worldbank','DIME / Development Impact · contratación de investigación','https://www.worldbank.org/en/about/unit/unit-dec/impactevaluation/JobOpenings',kind='canal',pay='varies',themes='causalidad,desigualdad',priority=1,fit='RA y análisis de impacto por proyecto: pregunta por diseño causal, código y colaboración con economistas.',watch='DIME es una unidad, no un segundo programa universal de prácticas. Sus internships pueden canalizarse por Pioneers.')
program('worldbank','Young Professionals Program','https://www.worldbank.org/ext/en/careers/talent-programs/young-professionals-program',stage='experiencia',duration='2 años',pay='salary',eligibility='Posgrado y 2–6 años de experiencia pertinente según las reglas consultadas; revisar cómo se computa la experiencia.',rhythm='Cohortes recurrentes.',themes='causalidad,desigualdad,clima',priority=3,fit='Gran ruta profesional en desarrollo. Para preparar una candidatura pronto, suele ser un compromiso mayor que una RA.',watch='No es un internship ni una vía automáticamente elegible tras el máster. Revalidar requisitos de experiencia de cada cohorte.')

institution('imf','FMI / IMF','economia','Estados Unidos','Washington DC',
'El organismo que trabaja en estabilidad macroeconómica, finanzas públicas y crisis. Aquí el idioma común es economía cuantitativa.',
'Muy fuerte para macro. Para plataformas y desigualdad micro, miraría antes una RA temática.',
'Trabajo con economistas, datos internacionales y problemas de política económica.',
'Prestigio macro no equivale a encaje con cualquier investigación social.',
'Frente a la OCDE es más macrofinanciero; frente al Banco Mundial, menos centrado en evaluar intervenciones de desarrollo.',
'https://www.imf.org/en/about/careers')
program('imf','Research Analyst Program','https://www.imf.org/en/about/recruitment/working-at-the-imf/research-analyst-program',duration='2 años',pay='salary',eligibility='Formación cuantitativa en economía o áreas relacionadas; criterios de la selección del RAP.',rhythm='Reclutamiento de programa; consultar instrucciones oficiales.',themes='macro,metodos',priority=2,fit='Potente para demostrar trabajo empírico con economistas. Su valor para CSS depende de la pregunta social que investigues.',watch='RAP y contratos individuales de Research Analyst son vías distintas. No presuponer elegibilidad ni convertir macro en social data science por el nombre.')
program('imf','Fund Internship Program · Economics','https://www.imf.org/en/about/careers/internship-program',stage='phd',duration='10–12 semanas',pay='salary',eligibility='Vía de economía dirigida a estudiantes de PhD; condiciones de edad y retorno a estudios en el portal.',rhythm='Programa de verano.',themes='macro,metodos',priority=4,fit='Investigación supervisada útil durante el doctorado.',watch='Las vías especializadas pueden admitir otros posgrados. No confundirlas con la elegibilidad de Economics.')

institution('ecb','Banco Central Europeo / ECB','economia','Alemania','Fráncfort',
'El banco central de la zona euro. Combina política monetaria, supervisión y producción de estadísticas.',
'Una opción seria si aterrizas en Research o Statistics.',
'Infraestructura de datos, economistas y problemas de medición.',
'Un equipo de operaciones o supervisión administrativa puede alejarte de una tesis.',
'Comparable al BIS en rigor macrofinanciero; más cerca de las instituciones europeas que de la agenda digital del OII.',
'https://www.ecb.europa.eu/careers/what-we-offer/traineeship/html/index.en.html')
program('ecb','Traineeship Programme','https://www.ecb.europa.eu/careers/what-we-offer/traineeship/html/index.en.html',duration='3–6 meses · posible extensión',pay='grant',eligibility='Grado; ciudadanía UE o país en adhesión; idiomas y límites de experiencia profesional según reglas.',rhythm='Convocatorias por equipo durante el año.',themes='macro,metodos',priority=2,fit='Prioriza investigación, estadística, microdatos, ML aplicado o economía digital.',watch='Distintas vacantes exigen niveles distintos. Una traineeship doctoral no es la misma que la general.')
program('ecb','Student Research Traineeship','https://www.ecb.europa.eu/pub/economic-research/programmes/traineeship/html/index.en.html',duration='Según programa',pay='grant',eligibility='Grado terminado y objetivo de cursar máster/PhD en economía o campo relacionado; revisar restricciones de etapa.',rhythm='La página indica solicitudes en el primer trimestre.',themes='macro,metodos',priority=2,fit='Diseñada para trabajar con economistas de DG Research y preparar estudios posteriores.',watch='Comprueba si tu historial de posgrado y la convocatoria concreta cumplen las condiciones.')
program('ecb','Graduate Programme','https://www.ecb.europa.eu/careers/what-we-offer/graduate/html/index.en.html',stage='phd',duration='Según cohorte',pay='salary',eligibility='El programa requiere PhD o estar próximo a completarlo; revisar reglas de cada edición.',rhythm='Cohortes.',themes='macro',priority=4,fit='Ruta profesional después del doctorado, no preparación previa.',watch='No confundir el término graduate con un programa abierto a cualquier graduado de máster.')

institution('bis','BIS / Banco de Pagos Internacionales','economia','Suiza','Basilea',
'El banco de los bancos centrales. Trabaja en estabilidad financiera, política monetaria y tecnología financiera.',
'Menos conocido fuera de economía; muy interesante dentro de ese mundo.',
'Institución pequeña, trabajo analítico e interlocutores de banca central.',
'La agenda financiera exige que puedas justificar el vínculo con tu pregunta social.',
'Más especializado que la OCDE y con una agenda de investigación comparable a bancos centrales.',
'https://www.bis.org/about/careers/early-careers')
program('bis','BIS Graduate Programme','https://www.bis.org/about/careers/early-careers',duration='Hasta 11 meses',pay='salary',eligibility='Grado o máster terminado recientemente; habilidades analíticas e inglés. Admite todas las nacionalidades.',rhythm='Suele anunciarse en primavera.',themes='macro,metodos',priority=2,fit='Economía, estadística y data science pueden darte una experiencia analítica convincente.',watch='El área concreta puede ser banca, tecnología o investigación. No asumir trabajo científico por pertenecer al BIS.')
program('bis','PhD Fellowship Programme','https://www.bis.org/about/careers/early-careers',stage='phd',duration='3–11 meses',pay='salary',eligibility='Matrícula de PhD en economía, finanzas o área relacionada; investigación y especialización relevantes.',rhythm='Suele anunciarse a finales de verano.',themes='macro',priority=4,fit='Proyecto de investigación durante el PhD.',watch='Necesitas estar cursando el doctorado; no es una predoc.')

institution('eib','BEI / European Investment Bank','economia','Luxemburgo','Luxemburgo · otras oficinas',
'El banco de inversión de la UE: financia infraestructuras, innovación y clima.',
'Gran nombre profesional; la señal académica depende de caer en evaluación o economía.',
'Datos de financiación e impacto de proyectos europeos.',
'Una rotación financiera no garantiza métodos ni autoría investigadora.',
'Más financiación de proyectos que BCE/BIS; menos investigación social transversal que OCDE.',
'https://www.eib.org/en/about/careers/categories/traineeships/index')
program('eib','Traineeships','https://www.eib.org/en/about/careers/categories/traineeships/index',duration='3–5 meses habitualmente',pay='grant',eligibility='Último año o recién graduado con experiencia limitada desde el último título; ciudadanía según reglas del BEI.',rhythm='Intakes y convocatorias por necesidades.',themes='clima,causalidad',priority=3,fit='Busca evaluación, economía, datos e innovación.',watch='Comprobar límites de experiencia y nacionalidad; no asumir que una plaza financiera produce un paper.')
program('eib','Graduate Programme','https://www.eib.org/en/about/careers/categories/graduate-programme.htm',duration='1–2 años habitualmente',pay='salary',eligibility='Título universitario y menos de 2 años de experiencia desde la graduación más reciente, con excepciones detalladas para prácticas.',rhythm='Convocatorias por área.',themes='clima,macro',priority=3,fit='Ruta de empleo para construir carrera en financiación pública.',watch='El coste de oportunidad para un PhD depende de tareas, supervisor y duración.')

institution('ebrd','BERD / EBRD','economia','Reino Unido','Londres · rotaciones regionales',
'Banco de desarrollo que invierte en economías en transición y proyectos del sector privado.',
'Una puerta londinense con dimensión internacional; vigila las rotaciones.',
'Evaluación, transformación digital y economía de proyectos.',
'Movilidad regional y tareas de inversión pueden dominar el trabajo.',
'Más orientado a inversión empresarial que Banco Mundial; ubicación inicial más conveniente para Londres.',
'https://www.ebrd.com/home/work-with-us/ebrd-careers/ebrd-international-professionals-programme.html')
program('ebrd','International Professionals Programme','https://www.ebrd.com/home/work-with-us/ebrd-careers/ebrd-international-professionals-programme.html',duration='24 meses',pay='salary',eligibility='Graduados con perfil y experiencia pertinentes; nacionalidad e idiomas según la convocatoria.',rhythm='Contratación por posiciones del IPP.',themes='clima,macro,ia',priority=3,fit='Prioriza Evaluation, Economics o Digital Transformation si existen en la cohorte.',watch='Londres no implica permanecer allí: puede haber rotación regional. No presuponer horario compatible con otro máster.')

for args in [
('afdb','Banco Africano de Desarrollo','Global','Abiyán · oficinas','Financia desarrollo africano: empleo, infraestructura y servicios.','Buena apuesta para investigación aplicada en África.','Economía del desarrollo y problemas con impacto social.','Elegibilidad por edad, nacionalidad y etapa; traslado según plaza.','Más regional que Banco Mundial; afinidad temática antes que jerarquía de marcas.','https://www.afdb.org/en/about-us/careers/internship-programme/eligibility-requirements'),
('adb','Asian Development Bank','Filipinas','Manila · oficinas','Banco multilateral de desarrollo de Asia y el Pacífico.','Míralo si quieres políticas y evaluación en Asia.','Asignaciones de investigación aplicada.','La práctica requiere seguir matriculado.','Comparable al AfDB o BID por especialización regional.','https://www.adb.org/work-with-us/careers/internship-program'),
('aiib','Asian Infrastructure Investment Bank','China','Pekín · modalidad por vía','Banco multilateral centrado en infraestructuras y sostenibilidad.','Interesa especialmente si la vía es Research/Academic.','Investigación aplicada e infraestructura sostenible.','Un puesto de inversión no equivale a una RA.','Más centrado en infraestructura que Banco Mundial; compara el proyecto concreto.','https://www.aiib.org/en/work-with-us/join-the-team/young-talent-programs/index.html'),
('idb','BID / Inter-American Development Bank','Global','Washington DC · América Latina','Banco de desarrollo de América Latina y el Caribe.','Potente para desigualdad, educación, trabajo y evaluación en la región.','Agenda social e investigación aplicada.','Prácticas ligadas a matrícula y permisos/nacionalidad.','El equivalente regional más natural al Banco Mundial si tu pregunta es latinoamericana.','https://www.iadb.org/en/how-we-can-work-together/students-recent-graduates'),
('esm','European Stability Mechanism','Luxemburgo','Luxemburgo','El fondo de rescate y estabilidad financiera de la zona euro.','Interesante si tu tesis conversa con crisis y política económica.','Economía aplicada en una institución especializada.','Menos afinidad directa con plataformas, redes o demografía.','Más acotado que BCE/BIS; no lo pondría primero para CSS generalista.','https://www.esm.europa.eu/content/how-do-traineeships-esm-work')]:
    id,name,country,city,intro,verdict,upside,downside,comp,url=args
    institution(id,name,'economia',country,city,intro,verdict,upside,downside,comp,url)
program('afdb','Internship Programme',institutions[-5]['url'],duration='Según sesión',pay='grant',eligibility='Máster en curso o obtenido en el último año; nacionalidad de país miembro y límite de edad de la edición.',rhythm='Sesiones recurrentes.',themes='causalidad,desigualdad,clima',priority=2,watch='La modalidad y la sede dependen de la asignación. Verificar edad a la fecha de referencia de cada sesión.')
program('afdb','Young Professionals Program','https://www.afdb.org/en/about-us/careers/young-professionals-program-ypp',stage='experiencia',duration='Programa de varios años',pay='salary',eligibility='Posgrado y experiencia pertinente; nacionalidad y edad según programa.',rhythm='Cohortes.',themes='clima,desigualdad',priority=3)
program('adb','Internship Program','https://www.adb.org/work-with-us/careers/internship-program',duration='8–12 semanas habitualmente',pay='grant',eligibility='Máster/PhD en curso durante toda la práctica; nacionalidad de país miembro y tema alineado.',rhythm='Ciclos de contratación.',themes='causalidad,clima,desigualdad',priority=2)
program('adb','Young Professionals Program','https://www.adb.org/work-with-us/careers/adb-young-professionals-program',stage='experiencia',duration='Según programa',pay='salary',eligibility='Posgrado, experiencia pertinente y nacionalidad de país miembro; edad según reglas.',rhythm='Cohortes.',themes='clima,macro',priority=3)
program('aiib','Global Internship Program','https://www.aiib.org/en/work-with-us/join-the-team/young-talent-programs/index.html',duration='Según vía y asignación',pay='grant',eligibility='Máster/PhD o graduación reciente en condiciones del programa.',rhythm='Selección anual de prácticas.',themes='clima,causalidad',priority=2,watch='Research/Academic y Corporate tienen tareas y modalidades distintas; remoto no equivale a cualquier país autorizado.')
program('aiib','Graduate Program','https://www.aiib.org/en/work-with-us/join-the-team/young-talent-programs/index.html',duration='2 años',pay='salary',eligibility='Posgrado y experiencia dentro de los límites del programa.',rhythm='Cohortes.',themes='clima,macro',priority=3)
program('idb','Internship Program','https://www.iadb.org/en/how-we-can-work-together/students-recent-graduates',duration='Según ciclo',pay='salary',eligibility='Estudiante activo; al menos 50% del posgrado cursado. Nacionalidad o permiso/residencia según la vía y oficina.',rhythm='Ciclos de invierno y verano; vías de país.',themes='causalidad,desigualdad',priority=2)
program('esm','Traineeships','https://www.esm.europa.eu/content/how-do-traineeships-esm-work',duration='6 meses · posible renovación de 6',pay='unknown',eligibility='Estudiante universitario o graduado en el último año de grado, máster o PhD.',rhythm='Convocatorias por equipo.',themes='macro',priority=3)

institution('jp','J-PAL','investigacion','Global','Europa · sedes y proyectos globales',
'La red de investigación que evalúa políticas contra la pobreza mediante experimentos y otros métodos de impacto.',
'Mi nº 1 si quieres aprender investigación causal trabajando con investigadores.',
'Datos, diseño de evaluación y referencias capaces de describir tu trabajo.',
'No todos los roles son científicos; en campo hay logística y gestión.',
'Más directo hacia una tesis empírica que una práctica multilateral genérica. DIME y una buena RA universitaria son los comparadores naturales.',
'https://www.povertyactionlab.org/page/careers-faq')
program('jp','General Data / Field Research Associate recruitment','https://www.povertyactionlab.org/page/recruitment-timeline',duration='Según puesto; frecuentemente compromiso prolongado',pay='salary',eligibility='Grado/máster y habilidades de análisis o trabajo de campo según proyecto; idiomas y permisos según sede.',rhythm='Reclutamiento coordinado y contratación por proyectos.',themes='causalidad,desigualdad,metodos',priority=1,fit='Data RA: código y análisis. Field RA: implementación y medición. Elige según la parte de investigación que necesitas demostrar.',watch='La aplicación común puede abarcar entidades asociadas. Ni publicación ni carta están garantizadas; pregunta por supervisor y responsabilidades.',docs='CV, expediente, motivación y referencias según la ronda.')
institution('ipa','Innovations for Poverty Action','investigacion','Global','Oficinas y proyectos de país',
'Organización que implementa investigación y evaluaciones de impacto con investigadores y responsables de políticas.',
'Gran alternativa a J-PAL; a veces el proyecto manda mucho más que la marca.',
'Trabajo sobre medición, encuestas, experimentos y política pública.',
'Tareas de campo y coordinación pueden ocupar una parte grande del puesto.',
'Más ejecución de proyectos de evaluación; compárala con J-PAL por investigador, datos y responsabilidad real.',
'https://poverty-action.org/current-opportunities')
program('ipa','Research Associate / Research Analyst · por proyecto','https://poverty-action.org/current-opportunities',kind='canal',pay='salary',themes='causalidad,desigualdad,metodos',priority=1,watch='Canal de contratación, no una práctica global con calendario fijo. Distingue evaluación, policy y operaciones.')

institution('lse','LSE · STICERD / CEP y equipos de investigación','investigacion','Reino Unido','Londres',
'Centros de economía aplicada sobre trabajo, desigualdad, ciudades, desarrollo y políticas públicas dentro de LSE.',
'Si encaja el supervisor, sería mi primera jugada en Londres.',
'Aprendes investigación al lado de quien puede evaluar tu contribución.',
'Una RA de economía no garantiza encaje con Computational Social Science ni admisión interna.',
'Más señal académica directa que una práctica institucional general. Para OII, busca preguntas sobre tecnología, trabajo o plataformas.',
'https://www.lse.ac.uk/economics/people/predocs')
program('lse','Pre-doctoral Research Assistants','https://www.lse.ac.uk/economics/people/predocs',duration='Según contrato de proyecto',pay='salary',eligibility='Formación cuantitativa, programación y economía/ciencias sociales según el investigador.',rhythm='Puestos predoc por grupos y proyectos; sin intake universal.',themes='causalidad,desigualdad,ia',priority=1,fit='Fuerte para ambos objetivos si haces investigación social computacional y obtienes una referencia concreta.',watch='El directorio documenta la vía predoc; no confirma futuras plazas. STICERD/CEP no son el comité de admisión del PhD CSS.')

institution('ifs','Institute for Fiscal Studies','investigacion','Reino Unido','Londres',
'Centro de investigación sobre impuestos, educación, desigualdad, familias y política pública.',
'Mi apuesta londinense más clara junto a una buena RA en LSE.',
'Microdatos, econometría y preguntas sociales con resultados públicos.',
'Necesitas una base económica sólida; no basta con saber entrenar modelos.',
'Más investigación económica empírica que un think tank de opinión; más próximo a desigualdad que BIS o FMI.',
'https://ifs.org.uk/jobs')
program('ifs','Research Economist · annual recruitment','https://ifs.org.uk/research-economists',duration='Empleo; condiciones del contrato',pay='salary',eligibility='Muy buen grado con componente sustancial de economía o máster pertinente.',rhythm='Reclutamiento anual.',themes='causalidad,desigualdad',priority=1,fit='Investigación económica profunda, análisis y comunicación pública: una buena preparación si tu PhD aborda problemas sociales.',watch='Es empleo de investigador, no un internship. Pregunta por proyectos, formación y horizonte de compromiso.')
program('ifs','Summer Internships','https://ifs.org.uk/summer-internships',duration='Verano',pay='unknown',eligibility='Estudiantes de economía interesados en investigación microeconómica; comprobar etapa concreta.',rhythm='Ronda anual, habitualmente desde otoño.',themes='causalidad,desigualdad',priority=2)

institution('mpidr','Max Planck · Demographic Research','investigacion','Alemania','Rostock',
'Instituto que estudia población, mortalidad, familias y cambio demográfico con métodos cuantitativos.',
'La joya menos obvia de este mapa para Social Data Science.',
'El Summer Incubator conecta datos computacionales, preguntas sociales y un proyecto de artículo.',
'Exige matrícula y residencia durante la estancia; escribir un artículo lleva más que un verano.',
'Más cerca de CSS y demografía que muchos programas con nombres más famosos.',
'https://incubator.demogr.mpg.de/')
program('mpidr','Population and Social Data Science Summer Incubator','https://incubator.demogr.mpg.de/Apply',duration='Aproximadamente 3 meses de verano',pay='grant',eligibility='Matrícula de máster/PhD durante la estancia; experiencia investigadora y aprobación del supervisor/administrador.',rhythm='Ediciones anuales documentadas.',themes='salud,desigualdad,metodos',priority=1,fit='Proyecto interdisciplinar que tiene como objetivo un artículo científico; muy buena historia para Oxford/LSE.',watch='El objetivo de publicación no es una publicación garantizada. Residencia presencial en Rostock y dedicación al proyecto.',docs='CV, carta, expedientes y datos de 2 referentes académicos, según edición.')

institution('ms','Microsoft Research','tecnologia','Global','Cambridge UK · EEUU · otros laboratorios',
'La rama de investigación de Microsoft, con trabajo científico en ML, sistemas y economía computacional.',
'Míralo por laboratorio: Economics and Computation es especialmente interesante para tu cruce de temas.',
'Mentoría de investigadores y problemas técnicos o económicos sustantivos.',
'El equipo y los permisos de publicación importan; el predoc económico está en EEUU.',
'Google ofrece más amplitud de equipos; MSR tiene una vía predoc explícita hacia computational social science.',
'https://www.microsoft.com/en-us/research/lab/microsoft-research-cambridge/internships/')
program('ms','Cambridge Research Internships','https://www.microsoft.com/en-us/research/lab/microsoft-research-cambridge/internships/',duration='Según proyecto',pay='salary',eligibility='Principalmente máster/PhD; grado considerado si encaja.',rhythm='Internships por equipos.',themes='ia,metodos,plataformas',priority=2,fit='Buena señal técnica. Para CSS, conecta el método con personas, mercados o instituciones.',watch='Cambridge no es Londres; comprueba presencialidad y especialidad. Publicación depende del proyecto.')
program('ms','Economics and Computation · Predoctoral Researchers','https://www.microsoft.com/en-us/research/theme/economics-and-computation/predoctoral-researchers/',duration='2 años · tiempo completo',pay='unknown',eligibility='Graduados recientes que preparan PhD en economía, information systems, CSS o computer science afín.',rhythm='Cohortes documentadas.',themes='plataformas,causalidad,ia',priority=1,fit='Una de las conexiones más explícitas empresa–PhD CSS. La página publica trayectorias posteriores de predocs.',watch='Cambridge, Massachusetts / Nueva York. Los destinos de antiguos participantes no son tasas ni garantía de admisión.',location='Cambridge Massachusetts · Nueva York')

for args in [
('uzh','Universidad de Zúrich · Economics','Suiza','Zúrich','Departamento con un programa predoc para preparar investigación doctoral.','Buena vía si economía y métodos son el centro de tu proyecto.','Trabajo con investigadores y preparación académica.','Hay que escoger tema; predoc económico no significa CSS generalista.','Comparable a LSE/CEMFI por la cercanía al investigador.','https://www.econ.uzh.ch/en/study/predoc.html'),
('cemfi','CEMFI','España','Madrid','Centro especializado en economía y finanzas con contratación predoc por proyectos.','Pequeño, concentrado y muy interesante si el proyecto encaja.','Microeconometría, datos de empleo, ciudades y desigualdad.','No hay intake universal de RA garantizado.','Más concentrado en economía que un instituto social amplio; compara con IFS/LSE por proyecto.','https://cemfi.es/forms-cemfi/jobmarket/jobmarket_offers.asp'),
('pse','Paris School of Economics','Francia','París','Red de investigación y formación económica con proyectos que contratan asistentes predoc.','Mira investigador y proyecto antes que el rótulo Paris.','Trabajo empírico, desarrollo, desigualdad y comercio.','Un anuncio histórico no prueba un programa global recurrente.','Comparable a CEMFI o LSE para RA económica; el encaje metodológico decide.','https://extranet.parisschoolofeconomics.eu/docs/koenig-pamina/respglob_predocs.pdf'),
('bocconi','Bocconi · IGIER / Dondena','Italia','Milán','Centros de economía y dinámica social donde existen trayectorias de asistentes de investigación.','Interesa por trabajo, población y comportamiento económico.','Investigación sobre fenómenos sociales y economía aplicada.','No consta aquí un programa predoc único verificado.','Dondena puede ser más social/demográfico; IGIER más económico.','https://www.unibocconi.it/en'),
('eui','European University Institute','Italia','Florencia / Fiesole','Instituto europeo de investigación en ciencias sociales y políticas.','Buen lugar si buscas un proyecto social sustantivo.','Equipos académicos y entorno de investigación internacional.','Traineeships administrativas y contratos RA son cosas distintas.','Más interdisciplinar que CEMFI; una RA temática puede acercarte a ambos PhD.','https://www.eui.eu/about/jobopportunities'),
('gesis','GESIS · Leibniz Institute for the Social Sciences','Alemania','Colonia · Mannheim','Infraestructura e investigación de métodos, encuestas y datos sociales.','Para metodología social, este nombre merece estar en tu radar.','Medición, calidad de datos y cruce computación–ciencias sociales.','Idiomas, matrícula local o requisitos de contrato pueden limitar la vía.','Más centrado en datos y métodos que un banco central; muy alineado con LSE Methodology.','https://www.gesis.org/en/institute/career/careers-at-gesis-we-are-seeking'),
('wzb','WZB · Berlin Social Science Center','Alemania','Berlín','Centro de investigación en instituciones, democracia, mercados y desigualdad.','Muy buena alternativa si tu tema es social de verdad.','Preguntas sociales y equipos empíricos.','Contratación por proyectos y posibles requisitos de alemán.','Más amplitud social que un predoc de economía; compara el método del grupo.','https://wzb.eu/en/the-wzb/working-at-the-wzb/job-opportunities'),
('weizenbaum','Weizenbaum Institute','Alemania','Berlín','Instituto de investigación sobre internet y sociedad digital.','Para plataformas, algoritmos y sociedad, tiene mucho sentido.','Temática directamente conectada con el OII.','No consta un internship general verificable en este atlas.','Más temáticamente digital que WZB; menos centrado en economía que IFS.','https://www.weizenbaum-institut.de/en/institute/work-and-career/jobs/'),
('zew','ZEW · Leibniz Centre for European Economic Research','Alemania','Mannheim','Centro de economía empírica y asesoramiento sobre innovación, empleo y políticas.','Una alternativa seria para economía de la innovación y del trabajo.','Proyectos aplicados y estudiantes asistentes.','Condiciones de prácticas y matrícula dependen del puesto.','Más economía aplicada que GESIS, que destaca en metodología social.','https://www.zew.de/en/career'),
('diw','DIW Berlin','Alemania','Berlín','Instituto de economía aplicada, desigualdad y datos de hogares, asociado al entorno SOEP.','Interesa mucho si quieres microdatos y política social.','Econometría, datos longitudinales y preguntas sobre desigualdad.','La vía de prácticas consultada exige prácticas obligatorias curriculares.','Más microdatos de hogares que BIS; compite con IFS por afinidad temática.','https://www.diw.de/en/diw_01.c.618535.en/careers/job_offers.html'),
('ifo','ifo Institute','Alemania','Múnich','Centro de investigación económica que estudia empleo, educación, innovación y economía pública.','Buena opción para trabajo empírico aplicado.','Diversidad de centros y conexiones con política económica.','No confundir prácticas de apoyo con una responsabilidad investigadora sustantiva.','Más economía y política que CSS amplio; el grupo concreto cambia la comparación.','https://www.ifo.de/en/career-ifo'),
('mpib','Max Planck · Human Development','Alemania','Berlín','Instituto de decisiones, comportamiento y desarrollo humano, con grupos computacionales.','Interesa si tu pregunta mezcla datos, conducta y decisiones.','Diseño experimental y modelización del comportamiento.','Prácticas por centro; no hay un único programa para todos los perfiles.','Más conducta y experimentos que MPIDR, que se centra en población.','https://www.mpib-berlin.mpg.de/909272/student-assistants-interns'),
('dfki','DFKI · Data Science and its Applications','Alemania','Alemania · por grupo','Centro alemán de IA aplicada con proyectos, tesis y prácticas de investigación.','Una vía técnica útil si encuentras una pregunta social que la sostenga.','Investigación computacional y tareas definidas por grupo.','La agenda puede estar lejos de ciencias sociales.','Más ingeniería que GESIS; compáralo con MSR por proyecto, no por país.','https://dsa.dfki.de/students/thesis-project-seminar/')]:
    id,name,country,city,intro,verdict,upside,downside,comp,url=args
    institution(id,name,'investigacion',country,city,intro,verdict,upside,downside,comp,url)
program('uzh','Pre-doctoral Programme','https://www.econ.uzh.ch/en/study/predoc.html',duration='Según puesto',pay='unknown',rhythm='Programa predoc; contratación por grupos.',themes='causalidad,desigualdad',priority=2)
for id,themes,priority in [('cemfi','causalidad,desigualdad',1),('pse','causalidad,desigualdad',2),('bocconi','desigualdad,salud',2),('eui','causalidad,desigualdad',2),('gesis','metodos,desigualdad',1),('wzb','desigualdad,causalidad',2),('weizenbaum','plataformas,ia',1),('zew','ia,causalidad',2),('ifo','causalidad,ia',2)]:
    i=next(x for x in institutions if x['id']==id)
    program(id,'Research / student assistant · por proyecto',i['url'],kind='canal',pay='varies',themes=themes,priority=priority,watch='Canal institucional o evidencia de contratación por proyecto, no programa fijo. Comprobar si exige matrícula, idioma o autorización local.')
program('diw','Prácticas curriculares obligatorias','https://www.diw.de/sixcms/detail.php?id=diw_01.c.418814.de',kind='canal',pay='unknown',eligibility='Matrícula y prácticas obligatorias exigidas por el plan de estudios.',themes='desigualdad,metodos',priority=2,watch='No presentar como un internship abierto a cualquier estudiante: la obligatoriedad curricular es una restricción real.')
program('mpib','Internships / student assistants · por centro','https://www.mpib-berlin.mpg.de/909272/student-assistants-interns',kind='canal',pay='unknown',themes='metodos,causalidad',priority=2)
program('dfki','Research internships / thesis projects','https://dsa.dfki.de/students/thesis-project-seminar/',kind='canal',pay='unknown',themes='ia,metodos',priority=3)

institution('iiasa','IIASA','investigacion','Austria','Laxenburg',
'Instituto internacional que modeliza sistemas sociales, ambientales y económicos a gran escala.',
'Para población, clima y sistemas, es muy interesante. Su YSSP va después de entrar al PhD.',
'Modelos y colaboración entre disciplinas.',
'YSSP requiere un proyecto doctoral y residencia; no sirve como predoc general.',
'Más modelización de sistemas que evaluación micro de J-PAL.',
'https://iiasa.ac.at/capacity-development/application-information')
program('iiasa','Young Scientists Summer Program (YSSP)','https://iiasa.ac.at/capacity-development/application-information',stage='phd',duration='3 meses · verano',pay='varies',eligibility='Estudiantes de PhD con proyecto relacionado; financiación según vías y país.',rhythm='Anual.',themes='clima,salud,metodos',priority=4,watch='Presencial en Laxenburg durante el programa. No asumir modalidad remota ni elegibilidad sin PhD.')

institution('turing','The Alan Turing Institute','investigacion','Reino Unido','Londres · por actividad',
'Instituto británico de data science e IA con proyectos y colaboración de investigación.',
'Buen entorno de métodos; verifica la etapa de cada programa.',
'Colaboración interdisciplinar y problemas de datos.',
'Muchas oportunidades estructuradas están dirigidas a doctorandos.',
'Más amplio en IA que GESIS; el vínculo social depende de la actividad.',
'https://www.turing.ac.uk/collaborate-turing/data-study-groups/get-involved-researcher')
program('turing','Data Study Groups','https://www.turing.ac.uk/collaborate-turing/data-study-groups/get-involved-researcher',duration='Actividad breve · según edición',pay='unknown',eligibility='Habitualmente doctorandos e investigadores iniciales; otras trayectorias según edición y habilidades.',rhythm='Ediciones por retos.',themes='ia,metodos',priority=3,fit='Experiencia de colaboración y un informe; complemento a una RA, no sustituto de investigación prolongada.',watch='Comprobar si la edición admite estudiantes de máster y qué producto final puedes conservar.')
program('turing','PhD Enrichment Scheme','https://www.turing.ac.uk/opportunities/doctoral-student-opportunities/phd-enrichment-scheme',stage='phd',duration='Según edición',pay='varies',eligibility='Doctorandos; universidades y otras condiciones según convocatoria.',rhythm='Esquema de estancias doctorales.',themes='ia,metodos',priority=4,watch='No es una vía previa a la admisión. Reconfirmar formato y continuidad del esquema.')

institution('oxford','Oxford Internet Institute · OII','investigacion','Reino Unido','Oxford · por proyecto',
'Instituto que estudia cómo internet, plataformas y tecnología cambian la sociedad. Es la casa del DPhil Social Data Science.',
'Para conocer investigación sobre tu tema, una RA aquí puede ser muy relevante.',
'Preguntas sociales digitales y proximidad temática al doctorado objetivo.',
'No consta una predoc universal ni una vía interna de admisión garantizada.',
'Más cercano a plataformas y vida digital que un predoc puramente macro.',
'https://www.oii.ox.ac.uk/')
program('oxford','RA en proyectos del OII / Fairwork','https://www.oii.ox.ac.uk/people/profiles/paul-povel/',kind='canal',pay='unknown',themes='plataformas,ia,desigualdad',priority=1,fit='La existencia de RA está documentada; sigue contratación del instituto y de proyectos con encaje real.',watch='El enlace documenta una trayectoria RA, no una plaza. No equivale a programa fijo ni garantiza entrada al DPhil.')

institution('sicss','SICSS · Summer Institutes in Computational Social Science','investigacion','Global','Sedes europeas y globales',
'Escuelas de verano que mezclan programación, métodos y preguntas sociales.',
'Buen complemento para aprender el idioma del campo y conocer investigadores.',
'Formación y red temática de CSS.',
'Una escuela corta no pesa como meses de trabajo investigador; requisitos cambian por sede.',
'Más CSS directo que un graduate scheme empresarial; menos experiencia que una RA.',
'https://sicss.io/apply')
program('sicss','Summer Institutes in Computational Social Science','https://sicss.io/apply',duration='Según sede · habitualmente breve',pay='varies',eligibility='Criterios por sede; suelen priorizar doctorandos y early career, con excepciones.',rhythm='Anual · sedes independientes.',themes='metodos,plataformas,causalidad',priority=3,fit='Para llenar huecos metodológicos y construir relaciones, no para sustituir la evidencia de investigación.',watch='No todas las sedes admiten máster ni ofrecen financiación; leer la página de la sede.')

# European institutions and agencies: the unit matters more than the umbrella.
institution('commission','Comisión Europea · Blue Book','europa','Bélgica / Luxemburgo','Bruselas · Luxemburgo · agencias',
'El ejecutivo de la UE. Eurostat, DG CNECT, EMPL y otros equipos trabajan con estadísticas y políticas digitales o sociales.',
'Una puerta conocida hacia política europea. Hay que elegir bien la unidad.',
'Política pública, instituciones y producción de datos.',
'El trabajo puede ser administrativo; la selección no asegura una unidad investigadora.',
'JRC es más científico; Blue Book general es más policy. Para tu PhD, la función pesa más que el sello UE.',
'https://traineeships.ec.europa.eu/index_en')
program('commission','Blue Book · Administrative traineeship','https://traineeships.ec.europa.eu/administrative-traineeship-university-graduates/eligibility-criteria-administrative-traineeship-university-graduates_en',duration='5 meses',pay='grant',eligibility='Grado completo; idiomas y límite de experiencia previa en instituciones UE. Cupos y reglas para nacionales no UE.',rhythm='Dos sesiones habituales al año.',themes='ia,desigualdad,metodos',priority=2,fit='Apunta a Eurostat, CNECT, EMPL, RTD o una unidad con análisis verificable.',watch='Eurostat no es un programa aparte: es posible destino de Blue Book. El acceso a datos y la autoría dependen de unidad.')
institution('jrc','Joint Research Centre · JRC','europa','UE · varias sedes','Ispra · Sevilla · otras sedes',
'El centro científico de la Comisión Europea: investigación que informa decisiones públicas.',
'Dentro de la UE, sería mi primera parada para hacer ciencia.',
'Modelización, evaluación, datos y política pública.',
'El área puede ser muy técnica o ajena a tu tema; hay que leer el proyecto.',
'Más investigación que Blue Book administrativo; compara con centros académicos por métodos y supervisor.',
'https://joint-research-centre.ec.europa.eu/work-us/training-and-workshops_en')
program('jrc','Scientific Traineeships','https://joint-research-centre.ec.europa.eu/work-us/training-and-workshops_en',duration='5 meses',pay='grant',eligibility='Graduados universitarios; nacionalidad, idiomas y restricciones según las reglas científicas del JRC.',rhythm='Dos sesiones habituales: marzo y octubre.',themes='ia,causalidad,clima',priority=1,fit='Muy buen puente ciencia–policy si el proyecto usa métodos computacionales para una pregunta social.',watch='Es una vía científica distinta de Blue Book. Algunas plazas no tienen contenido social.')

for args in [
('eurofound','Eurofound','Irlanda','Dublín','Agencia europea que investiga condiciones de vida y trabajo.','Uno de los nombres que más me interesan para IA y empleo.','Encuestas, mercado laboral y política social.','Equipo y producto final pueden variar.','Más trabajo/desigualdad que una institución UE general.','https://www.eurofound.europa.eu/en/pages/vacancies/information-on-traineeships'),
('cedefop','Cedefop','Grecia','Tesalónica','Agencia europea de formación, habilidades y mercado laboral.','Muy buen radar para skills y datos de anuncios laborales.','Indicadores de habilidades y empleo.','Duración larga y traslado; el rol concreto decide.','Más especializada en skills que Eurofound; ambas encajan con IA/trabajo.','https://www.cedefop.europa.eu/pt/about-cedefop/job-opportunities/trainees'),
('eea','European Environment Agency','Dinamarca','Copenhague','Agencia que reúne evidencia y datos sobre medio ambiente europeo.','Interesa si tu tema conecta personas, clima y territorio.','Datos, indicadores y política ambiental.','Puede dominar la ciencia ambiental sobre la social.','Más datos ambientales que JRC general; exige una pregunta social explícita.','https://www.eea.europa.eu/en/about/careers/traineeships'),
('fra','Fundamental Rights Agency · FRA','Austria','Viena','Agencia europea que produce evidencia sobre derechos, discriminación y desigualdad.','Apuesta temática para medición de desigualdad y derechos.','Encuestas sociales y evaluación de evidencia.','Modalidad y elegibilidad estrictas por convocatoria.','Más derechos/medición que economía; buen diálogo con LSE Methodology.','https://fra.europa.eu/en/about-fra/recruitment'),
('eige','European Institute for Gender Equality','Lituania','Vilna · oficina de Bruselas','Agencia europea que mide y analiza desigualdad de género.','Interesa para datos, indicadores y política de género.','Pregunta social clara y producción de indicadores.','Algunas plazas son comunicación o relaciones institucionales.','Más específica en género que Eurofound; busca la unidad de investigación.','https://eige.europa.eu/vacancy-types/traineeships?language_content_entity=en'),
('euspa','EU Agency for the Space Programme','Chequia','Praga · otras sedes','Agencia europea de programas espaciales y aplicaciones de datos satelitales.','Una vía lateral: buena si tienes una pregunta geoespacial social.','Datos de territorio y aplicaciones públicas.','Puede ser ingeniería, seguridad o administración.','Más operación espacial que ESA; compara el uso social de los datos.','https://www.euspa.europa.eu/node/9706')]:
    id,name,country,city,intro,verdict,upside,downside,comp,url=args
    institution(id,name,'europa',country,city,intro,verdict,upside,downside,comp,url)
    program(id,'Traineeships',url,duration='10 meses' if id=='cedefop' else 'Según esquema',pay='grant' if id in ['eurofound','cedefop'] else 'unknown',eligibility='Graduados; nacionalidad, idiomas, antigüedad del título y experiencia UE según reglas del organismo.',rhythm='Esquema institucional; convocatorias por edición.',themes={'eurofound':'ia,desigualdad,metodos','cedefop':'ia,metodos','eea':'clima,metodos','fra':'desigualdad,metodos','eige':'desigualdad,metodos','euspa':'clima,metodos'}[id],priority=1 if id in ['eurofound','cedefop'] else 2,watch='Verificar unidad, condiciones económicas y requisitos en las reglas de la edición. No se muestra disponibilidad actual.')
institution('parliament','Parlamento Europeo','europa','Bélgica / Luxemburgo','Bruselas · Luxemburgo · Estrasburgo',
'La institución elegida por los ciudadanos de la UE; analiza, debate y legisla.',
'Buen nombre en política europea; busca investigación parlamentaria si ese es tu objetivo.',
'Lectura de políticas, datos y comunicación con decisiones reales.',
'No todas las prácticas incluyen análisis original.',
'Más cerca del proceso político que JRC. Para una tesis, exige una función analítica clara.',
'https://www.europarl.europa.eu/at-your-service/en/work-with-us/traineeships')
program('parliament','Schuman Traineeships','https://www.europarl.europa.eu/at-your-service/en/work-with-us/traineeships',duration='5 meses',pay='grant',eligibility='Grado, idiomas y nacionalidad según reglas; limitaciones de experiencia previa en UE.',rhythm='Dos sesiones habituales al año.',themes='desigualdad,ia',priority=3,fit='Prioriza investigación parlamentaria, datos y evaluación de política; no asumir esas tareas en todas las plazas.')
institution('council','Consejo de la Unión Europea','europa','Bélgica','Bruselas',
'La institución donde se reúnen los gobiernos de los Estados de la UE.',
'Sirve para entender el poder institucional; la señal científica es más variable.',
'Experiencia de policy y negociación europea.',
'Menos garantía de trabajar con microdatos o investigación.',
'Más institucional que JRC/Eurofound; distinto del Consejo de Europa.',
'https://www.consilium.europa.eu/en/general-secretariat/careers/traineeships/')
program('council','Consilium Traineeships','https://www.consilium.europa.eu/en/general-secretariat/careers/traineeships/who-can-apply-for-a-traineeship/',duration='Según esquema',pay='grant',eligibility='Ciudadanía UE, grado y dos idiomas; límite estricto de experiencia previa en UE.',rhythm='Sesiones periódicas.',themes='desigualdad,ia',priority=3)
institution('eeas','EEAS · European External Action Service','europa','Global','Delegaciones de la UE',
'El servicio diplomático de la UE y sus delegaciones internacionales.',
'Buena ruta hacia relaciones internacionales; necesita un proyecto de datos para competir con una RA.',
'Trabajo en política exterior y desarrollo.',
'País de destino, ciudadanía y compromiso largo.',
'Más diplomacia que ciencia social computacional; se compara con JPO y policy fellowships.',
'https://www.eeas.europa.eu/eeas/vacancies_en?s=306')
program('eeas','Junior Professionals in Delegation (JPD)','https://www.eeas.europa.eu/eeas/call-expression-interest-junior-professionals-delegation-jpd-programme-2026-2028_en',duration='12 meses · renovable 12',pay='grant',eligibility='Ciudadanía UE, máster e inglés/francés; preselección nacional.',rhythm='Convocatoria aproximadamente bienal.',themes='desigualdad,clima',priority=3,watch='La página enlazada documenta una edición y sus reglas; no afirma disponibilidad ni fechas futuras.')
institution('coe','Consejo de Europa','europa','Francia','Estrasburgo · otras sedes',
'Organización de derechos humanos, democracia y Estado de derecho. No es una institución de la UE.',
'Interesa para derechos digitales y democracia; depende del equipo.',
'Perspectiva normativa y política sobre fenómenos sociales.',
'Una función administrativa aporta menos a una tesis cuantitativa.',
'Más derechos humanos que Consejo de la UE; menos investigación computacional que OII.',
'https://www.coe.int/en/web/jobs/traineeships')
program('coe','Traineeship Programme','https://www.coe.int/en/web/jobs/traineeships',pay='unknown',eligibility='Grado, ciudadanía de país miembro e idiomas según programa.',rhythm='Sesiones periódicas.',themes='ia,desigualdad',priority=3)
institution('osce','OSCE','europa','Global','Viena · misiones de campo',
'Organización de seguridad y cooperación con trabajo en elecciones, democracia y derechos.',
'Interesa si tu tema es desinformación, conflicto o instituciones.',
'Experiencia social y política en terreno.',
'Muchos roles son operativos y no metodológicos.',
'Más seguridad/democracia que desarrollo económico; compara con SIPRI según el tema.',
'https://jobs.osce.org/employment-modalities-fields-expertise')
program('osce','Internships','https://jobs.osce.org/employment-modalities-fields-expertise',duration='2–6 meses habitualmente',pay='unknown',eligibility='Último curso universitario o graduación reciente; edad y nacionalidad según reglas.',rhythm='Por necesidades de equipos.',themes='plataformas,desigualdad',priority=3)
program('osce','Junior Professional Officer Programme','https://jobs.osce.org/employment-modalities-fields-expertise',duration='Según esquema',pay='unknown',eligibility='Graduados con requisitos de nacionalidad, edad y patrocinio/selección según OSCE.',rhythm='Llamadas bienales documentadas.',themes='plataformas,desigualdad',priority=3)
institution('nato','NATO / OTAN','europa','Bélgica','Bruselas · sedes de la Alianza',
'Alianza política y militar con unidades de innovación, tecnología, análisis y política.',
'Sólo la pondría arriba si el tema es seguridad o información.',
'Acceso a problemas de seguridad y tecnología.',
'Ciudadanía, autorización de seguridad y posible limitación de difusión.',
'Más seguridad que OSCE y mucho más lejos de CSS generalista que una RA temática.',
'https://www.nato.int/internships')
program('nato','Internship Programme','https://www.nato.int/internships',duration='6 meses',pay='unknown',eligibility='Ciudadanía de país aliado, formación/edad y autorización de seguridad según programa.',rhythm='Programa recurrente.',themes='plataformas,ia',priority=3)
program('nato','Young Professionals Programme','https://www.nato.int/en/work-with-us/careers/young-professionals-programme',stage='experiencia',duration='3 años',pay='salary',eligibility='Posgrado, experiencia, edad y ciudadanía según edición.',rhythm='Cohortes.',themes='ia,plataformas',priority=4)
institution('esa','European Space Agency · ESA','europa','Europa · varias sedes','Sedes ESA',
'Agencia espacial europea: observación terrestre, tecnología y ciencia.',
'Vía lateral de calidad para datos geoespaciales; no es CSS por defecto.',
'Técnica y datos de observación del territorio.',
'Para tu PhD hace falta una pregunta social: ciudades, pobreza, clima o accesibilidad.',
'Más investigación/tecnología espacial que EUSPA. Elige aplicaciones sociales y ambientales.',
'https://www.esa.int/About_Us/Careers_at_ESA/Entry-level_and_research_programmes')
program('esa','ESA Graduate Trainee Programme','https://www.esa.int/About_Us/Careers_at_ESA/Entry-level_and_research_programmes',duration='Según programa',pay='salary',eligibility='Finalizando máster o recién graduado; ciudadanía de países elegibles ESA.',rhythm='Programa de cohortes.',themes='clima,metodos',priority=3)
program('esa','Student Internships','https://www.esa.int/About_Us/Careers_at_ESA/Entry-level_and_research_programmes',pay='unknown',eligibility='Estudiantes; etapa y nacionalidad según reglas.',rhythm='Esquema de prácticas para estudiantes.',themes='clima,metodos',priority=3)

# UN system, deliberately separated by organisation: pay is not uniform.
for args in [
('undp','UNDP / PNUD','Global','Oficinas globales · modalidad por puesto','Agencia de desarrollo que trabaja con gobiernos en gobernanza, pobreza, clima y digitalización.','Interesa en datos, evaluación o transformación digital.','Problemas sociales reales y trabajo con gobiernos.','Hay mucho trabajo de operaciones; el título intern no dice qué vas a hacer.','Más desarrollo institucional que J-PAL; busca equipos analíticos.','https://www.undp.org/careers/people-programmes'),
('unicef','UNICEF','Global','Sedes y oficinas · Innocenti','Agencia de infancia: salud, educación, protección y evidencia sobre niños y jóvenes.','Uno de los destinos ONU más claros para datos sociales.','Datos, encuestas y preguntas sociales sustantivas.','No todas las prácticas son de investigación.','Más infancia que UNDP; Innocenti y Data & Analytics son destinos a explorar.','https://www.unicef.org/careers/internships'),
('ilo','OIT / ILO','Suiza','Ginebra · oficinas','La agencia del trabajo: empleo, condiciones laborales y estadísticas.','Para IA y trabajo, me interesa más que una ONU genérica.','Tema muy conectado con plataformas y mercado laboral.','Restricciones de etapa y financiación que conviene leer.','Más especializado en trabajo que OCDE; ambas se comparan por unidad y producto.','https://jobs.ilo.org/content/Internships/'),
('unesco','UNESCO','Francia','París · otras sedes','Educación, ciencia, cultura y normas sobre tecnología, incluida ética de IA.','Buen tema; la falta de pago baja mi prioridad práctica.','Educación e instituciones científicas.','Las prácticas no se remuneran; el pool no garantiza asignación.','Más normativa/educación que investigación causal.','https://careers.unesco.org/content/Internship-Programme/'),
('unhcr','UNHCR / ACNUR','Global','Ginebra · oficinas de país','Agencia de refugiados y desplazamiento forzado.','Muy interesante si quieres estudiar migración y medición social.','Datos de desplazamiento, encuestas y problemas de protección.','Una práctica de apoyo operativo puede tener poca autonomía analítica.','Más migración/protección que UNDP; comparar con IOM según el equipo.','https://www.unhcr.org/pages/49c3646c49d.html'),
('unfpa','UNFPA','Global','Sedes y oficinas de país','Fondo de población: demografía, salud reproductiva y desigualdad.','Buen encaje temático para población y datos.','Problemas demográficos y medición.','Asignación a un roster no garantiza equipo ni plaza.','Más población/salud que UNICEF, que prioriza infancia.','https://www.unfpa.org/jobs/global-internship-roster-2026'),
('fao','FAO','Italia','Roma · oficinas','Agencia de alimentación y agricultura con estadísticas sobre sistemas alimentarios.','Interesa si conectas alimentos, pobreza, territorio y clima.','Estadística y política de desarrollo.','Elegibilidad por edad, nacionalidad y formación; equipo muy variable.','Más sistemas alimentarios que Banco Mundial general.','https://www.fao.org/employment/young-talent-programme/internship-programme/'),
('wfp','World Food Programme / PMA','Italia','Roma · operaciones globales','Organización de ayuda alimentaria y respuesta humanitaria.','Para datos humanitarios puede ser potente; pide trabajo analítico concreto.','Operaciones con datos y medición de necesidades.','La urgencia operativa puede desplazar objetivos de investigación.','Más operación humanitaria que FAO; compara función, no sólo nombre.','https://www.wfp.org/careers/contract-types'),
('who','OMS / WHO','Suiza','Ginebra · oficinas','Agencia de salud pública que trabaja con indicadores, sistemas sanitarios y evidencia.','Buen destino para salud y desigualdad si el equipo investiga.','Preguntas de salud con métodos estadísticos.','Condiciones de financiación y continuidad deben verificarse.','Más salud que UNDP; para una tesis, compara con grupos académicos de población.','https://www.who.int/careers/internship-programme'),
('wider','UNU-WIDER','Finlandia','Helsinki','Instituto de la Universidad de Naciones Unidas dedicado a economía del desarrollo.','Más investigación que muchas otras entradas del sistema ONU.','Desigualdad, desarrollo y trabajo académico.','Las prácticas generales y la estancia doctoral son vías distintas.','Comparable a centros de desarrollo; más científico que una práctica administrativa ONU.','https://www.wider.unu.edu/opportunity/unu-wider-internship-programme'),
('unssc','UN System Staff College','Italia','Turín · Bonn','Centro de aprendizaje y desarrollo de capacidades del sistema ONU.','Una vía de formación y organización; menos directa para una tesis cuantitativa.','Entorno multilateral y proyectos de aprendizaje.','No asumir investigación original en todas las prácticas.','Más formación institucional que UNU-WIDER.','https://www.unssc.org/about/employment-opportunities/internship-programme')]:
    id,name,country,city,intro,verdict,upside,downside,comp,url=args
    institution(id,name,'multilateral',country,city,intro,verdict,upside,downside,comp,url)
details={
'undp':('Hasta 6 meses habitualmente','grant','Máster, último año de grado o graduado en el último año.','ia,causalidad,desigualdad'),
'unicef':('6–26 semanas','grant','Estudiante o graduado en los últimos 2 años; idiomas y edad según reglas.','salud,desigualdad,metodos'),
'ilo':('3–6 meses','grant','Último año de máster/posgrado o graduado del último año; idiomas pertinentes.','ia,desigualdad,metodos'),
'unesco':('1–6 meses','unpaid','Máster en curso o titulado en los últimos 12 meses; edad e idiomas según reglas.','ia,metodos'),
'unhcr':('Según asignación','grant','Estudiante o graduado reciente; formación, idiomas y reglas familiares.','desigualdad,metodos'),
'unfpa':('Según asignación','grant','Estudiantes y graduados recientes según reglas del roster.','salud,desigualdad'),
'fao':('Según asignación','grant','Estudiante o graduado reciente; ciudadanía de país miembro, edad e idiomas.','clima,desigualdad,metodos'),
'wfp':('Según asignación','grant','Estudiantes o graduados recientes; formación y matrícula según reglas.','clima,desigualdad,metodos'),
'who':('Según asignación','varies','Estudiante o graduado reciente; formación y otros criterios del programa.','salud,metodos'),
'wider':('Según programa','unknown','Estudiantes/graduados según reglas de internship.','desigualdad,causalidad'),
'unssc':('Según asignación','unknown','Posgrado en curso o graduación reciente e inglés, según programa.','metodos,desigualdad')}
for id,(duration,pay,eligibility,themes) in details.items():
    i=next(x for x in institutions if x['id']==id)
    program(id,'Internship Programme',i['url'],duration=duration,pay=pay,eligibility=eligibility,themes=themes,priority=2 if id in ['unicef','ilo','wider'] else 3,
    rhythm='Roster habitual de abril y octubre; asignaciones durante el año.' if id=='ilo' else 'Política institucional de prácticas; asignación por equipos.',
    watch='La agencia y el equipo determinan modalidad, tareas y remuneración. Remoto no implica autorización automática para trabajar desde UK.')
program('undp','Graduate Programme','https://www.undp.org/careers/people-programmes',duration='Según cohorte',pay='salary',eligibility='Nacionales de países donde UNDP desarrolla programas; estudios y experiencia según reglas.',rhythm='Cohortes.',themes='desigualdad,ia',priority=3,watch='No está abierto automáticamente a cualquier nacionalidad; comprobar país elegible.')
program('wider','Visiting PhD Fellowship','https://www.wider.unu.edu/opportunity/visiting-phd-fellowship',stage='phd',duration='Estancia doctoral',pay='varies',eligibility='Doctorandos con investigación en economía del desarrollo.',rhythm='Rondas de fellowship.',themes='desigualdad,causalidad',priority=4,watch='La antigua denominación PhD Internship no debe confundirse con una práctica de máster.')

institution('un','Secretaría de Naciones Unidas','multilateral','Global','Nueva York · Ginebra · sedes regionales',
'El núcleo administrativo de Naciones Unidas: incluye áreas de estadística, desarrollo y asuntos humanitarios.',
'Un nombre amplio. El departamento y las tareas son la decisión real.',
'Problemas públicos y datos internacionales.',
'Muchas prácticas de la Secretaría no tienen pago; no generalizar esa regla a todas las agencias.',
'Más heterogénea que ILO/UNICEF; DESA, UNECE, UNCTAD, CEPAL y OCHA son unidades temáticas a explorar.',
'https://www.un.org/en/get-involved/')
program('un','Secretariat Internships','https://www.un.org/en/get-involved/',pay='unpaid',eligibility='Formación y graduación según reglas de internships de la Secretaría y convocatoria.',rhythm='Por departamentos y necesidades.',themes='metodos,desigualdad,plataformas',priority=3,watch='Pago indicado para el esquema general de Secretaría; revisar excepciones. Evitar prácticas puramente administrativas si el objetivo es el PhD.')
program('un','Young Professionals Programme','https://careers.un.org/ypp?language=en',duration='Proceso de examen y posible contratación',pay='salary',eligibility='Nacionalidad de país participante del año, edad, título pertinente e inglés/francés.',rhythm='Examen anual; países y áreas cambian.',themes='metodos,desigualdad',priority=3,watch='Estar en un roster no garantiza contratación; la lista de países se consulta en el portal, no se predice aquí.')
institution('jpo','JPO · sistema ONU','multilateral','Global','Agencias y países según patrocinador',
'Mecanismo de puestos Junior Professional Officer financiados por países donantes, con reglas nacionales.',
'Gran vía multilateral si cumples el patrocinio; no es un internship universal.',
'Trabajo profesional con supervisión y especialización.',
'Nacionalidad, edad y experiencia dependen del país patrocinador.',
'Más contrato profesional que práctica; compara con YPP y graduate programmes.',
'https://jpo.desa.un.org/')
program('jpo','Junior Professional Officer Programme','https://jpo.desa.un.org/',stage='experiencia',duration='Según patrocinador y contrato',pay='salary',eligibility='Normalmente posgrado y experiencia; nacionalidad/edad según convocatoria del donante.',rhythm='Convocatorias nacionales y de organismos.',themes='desigualdad,ia,metodos',priority=3)
institution('unv','UN Volunteers','multilateral','Global','Global · vía online',
'El programa de voluntariado de la ONU: asignaciones profesionales y tareas online son modalidades distintas.',
'La vía online puede darte un proyecto; no la confundas con empleo ni con una RA.',
'Entrada a tareas aplicadas y posibilidad de trabajo a distancia en la vía online.',
'La experiencia de una tarea corta y voluntaria tiene límites como señal académica.',
'Menos continuidad que un internship estructurado; útil si el producto y la supervisión son claros.',
'https://www.unv.org/conditions-service')
program('unv','Online Volunteering','https://explore.unv.org/ov-doa-criteria',kind='canal',duration='Por tarea',pay='unpaid',eligibility='Habilidades y requisitos de cada tarea.',themes='metodos,desigualdad',priority=3,fit='Un pequeño proyecto reproducible puede ayudar, pero no tiene la intensidad ni el contrato de una RA.',watch='Voluntariado online no significa empleo ONU. Confirmar interlocutor, derechos de difusión y tareas.')
program('unv','UN Volunteer assignments','https://www.unv.org/conditions-service',kind='canal',pay='varies',eligibility='Categorías y experiencia según las condiciones de servicio actualizadas; reglas por asignación.',themes='desigualdad,metodos',priority=3,watch='No usar categorías antiguas de Youth Volunteers como si fueran las vigentes. Asignaciones remuneradas con prestaciones no son salarios de staff ONU.')
institution('wto','OMC / WTO','multilateral','Suiza','Ginebra',
'El organismo de las reglas del comercio internacional, con análisis de flujos y política comercial.',
'Interesa para comercio, empleo y empresas; menos directo para otras ramas de CSS.',
'Economía internacional y comparaciones entre países.',
'Elegibilidad especializada y trabajo no siempre investigativo.',
'Más comercio que FMI; menos agenda social transversal que OCDE.',
'https://www.wto.org/english/thewto_e/vacan_e/vacan_e.htm')
program('wto','WTO Internship Programme','https://www.wto.org/english/thewto_e/vacan_e/faq_e.htm',pay='unknown',eligibility='Posgrado o graduación avanzada reciente, nacionalidad y edad según programa.',rhythm='Programa institucional por necesidades.',themes='macro,desigualdad',priority=3)
program('wto','Young Professionals Programme','https://www.wto.org/english/thewto_e/vacan_e/vacan_e.htm',stage='experiencia',pay='salary',eligibility='Nacionales de miembros infrarrepresentados, posgrado y experiencia según convocatoria.',rhythm='Cohortes.',themes='macro',priority=3)

for id,name,intro,city,url,themes in [
('iom','IOM / OIM','Organización de migraciones. Su Displacement Tracking Matrix mide desplazamiento y necesidades.','Ginebra · oficinas','https://dtm.iom.int/vacancy-status/open','desigualdad,metodos'),
('unops','UNOPS','Organización de gestión de proyectos, infraestructura y servicios para el sistema ONU.','Copenhague · oficinas','https://jobs.unops.org/','clima,metodos'),
('itu','ITU / UIT','Organismo de telecomunicaciones: conectividad, estándares e indicadores digitales.','Ginebra','https://jobs.itu.int/','ia,metodos')]:
    institution(id,name,'multilateral','Global',city,intro,'Interesa por un equipo de datos concreto, no por la sigla a secas.','Problemas públicos y datos aplicados.','No se verifica aquí una cohorte global homogénea; condiciones por puesto.','Compara con agencias más cercanas a tu tema y con RA académicas.',url)
    program(id,'Prácticas / contratación por equipos',url,kind='canal',pay='varies',themes=themes,priority=3,watch='Portal de contratación o evidencia de internship, no lista de vacantes de este atlas. No asumir condiciones iguales entre equipos.')

# Policy and AI governance.
for args in [
('chatham','Chatham House','Reino Unido','Londres','Think tank de asuntos internacionales y debate de políticas.','Nombre reconocible en policy; el equipo investigador decide para tu PhD.','Mentoría, análisis político y red de expertos.','También hay eventos y comunicación; no toda práctica hace investigación.','Más policy internacional que IFS; menos econometría por defecto.','https://www.chathamhouse.org/academy/internships'),
('odi','ODI Global','Global','Gobiernos de países participantes','Centro de desarrollo cuyo Fellowship coloca economistas y estadísticos en gobiernos.','Mi primera opción de esta familia si quieres política cuantitativa en terreno.','Responsabilidad aplicada y conocimiento institucional.','Dos años y disposición a trasladarse; publicación no garantizada.','Más inmersión profesional que una RA; menos foco en paper que J-PAL.','https://odi.org/en/fellowship-scheme/'),
('govai','Centre for the Governance of AI · GovAI','Reino Unido','UK · vía específica en Washington','Centro de investigación sobre gobernanza de inteligencia artificial.','Interesa para una tesis de IA y sociedad; elige Research Track.','Proyecto supervisado y agenda directamente relacionada con IA.','Applied Track puede ser gestión o política; el campo tiene una agenda específica.','Más governance que ML técnico; más cercano a OII que una internship de ingeniería.','https://www.governance.ai/opportunities'),
('bruegel','Bruegel','Bélgica','Bruselas','Think tank especializado en economía y política europea.','Buen radar para economía digital, energía y políticas.','Análisis con economistas y productos públicos.','Roles por necesidad; distinguir investigación y apoyo institucional.','Más económico que Chatham House; más policy que una RA universitaria.','https://www.bruegel.org/'),
('ceps','Centre for European Policy Studies · CEPS','Bélgica','Bruselas','Think tank de políticas europeas, regulación y economía.','Interesa si puedes trabajar en regulación y datos.','Problemas europeos y equipos temáticos.','Un internship de eventos o partnerships aporta poco a una tesis.','Más UE/regulación que Chatham; compara departamento y métodos.','https://www.ceps.eu/about-ceps/career-opportunities/'),
('sipri','SIPRI','Suecia','Estocolmo','Instituto de investigación sobre paz, seguridad y armamento, conocido por sus bases de datos.','Buena ruta si tu pregunta es conflicto, redes o información.','Datos y agenda de investigación definida.','Prácticas según necesidad, sin programa universal asegurado.','Más investigación empírica de seguridad que una práctica diplomática general.','https://www.sipri.org/about/vacancies'),
('rand','RAND Europe','Reino Unido / Bélgica','Cambridge · Bruselas','Organización de investigación aplicada para decisiones de política pública.','Interesa por evaluación y métodos, siempre mirando el proyecto.','Informes, evaluación y problemas públicos.','Investigación por encargo puede limitar libertad y publicación académica.','Más evaluación aplicada que think tank de opinión; distinto de RAND USA y su summer programme.','https://www.rand.org/randeurope.html'),
('ada','Ada Lovelace Institute','Reino Unido','Londres','Instituto que estudia los efectos sociales de datos e IA.','Muy buen encaje temático para OII; la vía es contratación por proyectos.','Gobernanza, derechos, percepción social y evidencia sobre IA.','No consta un internship global fijo verificado.','Más IA/sociedad que ODI Global; menos ingeniería que Turing.','https://www.adalovelaceinstitute.org/about/jobs/'),
('nesta','Nesta','Reino Unido','Londres · por equipo','Organización de innovación con trabajo en políticas, comportamiento y datos.','Interesa cuando la tarea es evaluación o análisis, no sólo innovación de nombre.','Problemas públicos y métodos aplicados.','El programa de prácticas documentado puede cambiar o no repetirse en una edición futura.','Más innovación aplicada que IFS; exige aclarar la parte de investigación.','https://www.nesta.org.uk/internship-programme/'),
('opendata','Open Data Institute · ODI','Reino Unido','Londres','Instituto de datos abiertos, gobernanza y ecosistemas de datos.','Útil para gobernanza de datos; ojo con confundir los dos ODI.','Datos, estándares y política digital.','No es el ODI Global del Fellowship de economistas.','Más ecosistema de datos que economía del desarrollo.','https://theodi.org/about-the-odi/work-with-us/'),
('owid','Our World in Data','Reino Unido','Por empleo y equipo','Publicación de investigación y visualización con datos sobre problemas globales.','Un buen portfolio público; no ofrece un internship para entrar por atajo.','Reproducibilidad, comunicación y análisis de datos.','Su FAQ indica que no ofrece internships ni voluntariado.','Más publicación de datos que centro de formación; busca empleo pertinente.','https://ourworldindata.org/faqs'),
('cgd','Center for Global Development','Global','Londres · Washington','Centro de investigación y política de desarrollo.','Otra alternativa que miraría para investigación aplicada.','Problemas de desarrollo, economía y evidencia.','Contratación por puestos; ninguna RA se presupone permanente.','Más policy que predoc formal; compara supervisor y responsabilidades con J-PAL/IFS.','https://www.cgdev.org/careers')]:
    id,name,country,city,intro,verdict,upside,downside,comp,url=args
    institution(id,name,'policy',country,city,intro,verdict,upside,downside,comp,url)
program('chatham','Academy Internships','https://www.chathamhouse.org/academy/internships',duration='6 meses',pay='salary',eligibility='Estudiantes y graduados según convocatoria; autorización de trabajo y otras condiciones.',rhythm='Programa recurrente, plazas limitadas por edición.',themes='plataformas,ia,desigualdad',priority=3,watch='London Living Wage según la página; verificar la edición. Tiempo completo/parcial y tareas según equipo.')
program('chatham','Academy Fellowships','https://www.chathamhouse.org/academy/fellowships',stage='experiencia',duration='Hasta 10 meses según fellowship',pay='varies',eligibility='Criterios de experiencia, región o afiliación según fellowship.',rhythm='Cohortes y fellowships específicos.',themes='plataformas,ia',priority=3)
program('odi','ODI Fellowship Scheme','https://odi.org/en/fellowship-scheme/',duration='2 años',pay='salary',eligibility='Máster/PhD en economía, estadística o campo relacionado; disposición a destinos participantes.',rhythm='Cohortes recurrentes.',themes='causalidad,desigualdad,metodos',priority=2,fit='Experiencia económica/estadística dentro de gobiernos: excelente para policy, potencial académico si puedes documentar investigación.',watch='No es una estancia londinense. La disposición a trabajar en países participantes es central.')
program('govai','Summer / Winter Fellowship · Research Track','https://www.governance.ai/opportunities',duration='3 meses',pay='varies',eligibility='Perfil y proyecto adecuados; no suponer un título obligatorio universal.',rhythm='Fellowships de verano e invierno.',themes='ia,plataformas',priority=1,fit='Una pregunta de gobernanza de IA, un supervisor y un resultado investigativo claro pueden conectar muy bien con OII.',watch='La etiqueta Applied Track no garantiza investigación: puede centrarse en gestión o policy. Ubicación UK depende de la vía.')
for id,themes in [('bruegel','macro,ia,clima'),('ceps','ia,clima'),('sipri','plataformas,metodos'),('rand','causalidad,desigualdad'),('ada','ia,desigualdad'),('nesta','causalidad,ia'),('opendata','ia,metodos'),('owid','metodos,desigualdad'),('cgd','causalidad,desigualdad')]:
    i=next(x for x in institutions if x['id']==id)
    url='https://ourworldindata.org/jobs' if id=='owid' else i['url']
    program(id,'Research / junior roles · por equipo',url,kind='canal',pay='unknown',themes=themes,priority=2,
    watch='Contratación por equipo; no se confirma un calendario recurrente fijo. Our World in Data no ofrece internships ni voluntariado.' if id=='owid' else 'Canal de contratación. No se promete programa fijo, plaza ni edición futura; verificar si las tareas son investigación.')

# Technical companies: no generic FAANG ranking.
for args in [
('google','Google Research / Google DeepMind','Global','Londres · Zúrich · otras sedes','Equipos de investigación en IA y computación dentro de Google.','Muy fuerte en métodos; hace falta conectar el proyecto con una pregunta social.','Investigadores, infraestructura y problemas computacionales.','Ni todo Google es research ni todo research es CSS; datos y publicación pueden estar limitados.','Frente a MSR, más amplitud de equipos; la elección es mentor, proyecto y resultado.','https://deepmind.google/student-researcher-program/'),
('amazon','Amazon Science','Global','Europa · EEUU · por equipo','Equipos científicos sobre decisiones, mercados, lenguaje, recomendación y operaciones.','Interesa si el proyecto es experimental, económico o metodológico.','Sistemas reales, datos y ciencia aplicada.','El objetivo de producto puede dominar el problema académico.','Más producto/decisiones que investigación de policy; compara con MSR por grupo.','https://www.amazon.science/careers'),
('meta','Meta','Global','Londres · otras sedes','Empresa de plataformas sociales con equipos de IA, producto y research.','Su objeto de estudio encaja con CSS; el acceso y la autonomía no vienen gratis.','Redes, experimentos, recomendación e IA.','Research internship no es siempre accesible antes del PhD; publicación y datos dependen del equipo.','Más plataformas sociales que NVIDIA; compara equipo y restricciones con Google.','https://www.metacareers.com/teams/technology?tab=AI'),
('ibm','IBM Research Europe','Suiza','Zúrich · otros laboratorios','Laboratorios de investigación en IA, algoritmos y computación.','Buena vía técnica si el proyecto tiene aplicación social convincente.','Investigación industrial y vínculos académicos.','Muchos temas son hardware o computación, lejos de CSS.','Más laboratorio científico que consultoría; el tema manda frente a Google/MSR.','https://research.ibm.com/labs/zurich'),
('spotify','Spotify','Reino Unido / Suecia','Londres · Estocolmo · otras sedes','Plataforma de audio con investigación en recomendaciones y comportamiento de usuarios.','Interesa para plataformas, preferencias y experimentación.','Objeto social reconocible y problemas de recomendación.','El internship concreto puede exigir PhD o centrarse en producto.','Más comportamiento de consumo cultural que macro/policy; compara con Meta según pregunta.','https://www.lifeatspotify.com/find-your-team/job-categories/data-research-insights'),
('nvidia','NVIDIA Research','Global','Por laboratorio','Investigación en ML y computación acelerada.','Gran señal técnica, pero un desvío si no hay pregunta social.','Métodos y sistemas computacionales.','El encaje con ciencias sociales suele ser indirecto.','Más infraestructura de IA que gobernanza o medición social.','https://www.nvidia.com/en-us/research/internships/'),
('openai','OpenAI','Estados Unidos','Según Residency · verificar sede','Laboratorio y empresa de IA con investigación y producto.','La Residency es una ruta intensiva de IA; para CSS hay que elegir un problema social.','Mentoría e investigación técnica.','Traslado, dedicación y restricciones de difusión; no asumir simultaneidad con estudios.','Más investigación de modelos que política social; distinta de GovAI.','https://openai.com/residency/'),
('anthropic','Anthropic','Global','Según programa','Empresa de IA con investigación en seguridad y comportamiento de modelos.','El Fellows Program interesa si tu pregunta es seguridad empírica o evaluación de IA.','Proyecto de investigación y mentoría en seguridad.','La agenda de AI safety no cubre toda la ciencia social de datos.','Más seguridad de modelos que GovAI, que estudia gobernanza e instituciones.','https://alignment.anthropic.com/2024/anthropic-fellows-program/')]:
    id,name,country,city,intro,verdict,upside,downside,comp,url=args
    institution(id,name,'tecnologia',country,city,intro,verdict,upside,downside,comp,url)
program('google','Student Researcher Program','https://deepmind.google/student-researcher-program/',duration='Según equipo y contrato',pay='unknown',eligibility='Matrícula de grado, máster o PhD; aplicaciones por nivel y lugar.',rhythm='Vía institucional de contratación de estudiantes.',themes='ia,plataformas,metodos',priority=2,fit='Buena señal técnica. Para Oxford/LSE, argumenta qué fenómeno social investigaste y cómo.',watch='El programa puede asignarte a DeepMind, Google Research u otros equipos. No equivale a una plaza específica de DeepMind.')
program('amazon','Applied / Research Science Internships','https://www.amazon.science/careers',duration='Según asignación',pay='unknown',eligibility='Máster o PhD según el puesto; algunos tracks exigen PhD.',rhythm='Internships de science por equipo.',themes='ia,plataformas,causalidad',priority=2,watch='La elegibilidad de una internship no se puede extrapolar a todas. Busca economía, experimentación o métodos con relevancia social.')
program('meta','Research Internships · por equipo','https://www.metacareers.com/teams/technology?tab=AI',kind='canal',pay='unknown',eligibility='Nivel académico y capacidades según equipo; frecuentes puestos de investigación para doctorandos.',themes='plataformas,ia',priority=2,watch='Portal de investigación y contratación; este atlas no certifica un programa único de máster ni un intake europeo fijo.')
program('ibm','Research internships / summer students','https://research.ibm.com/labs/zurich',kind='canal',pay='unknown',themes='ia,metodos',priority=2,watch='El laboratorio documenta summer students e internships; contratación y condiciones por proyecto.')
program('spotify','Internship programme · Data, Research & Insights','https://www.lifeatspotify.com/find-your-team/job-categories/data-research-insights',kind='canal',pay='unknown',themes='plataformas,causalidad',priority=2,watch='No usar un anuncio de una conferencia como convocatoria general. Verificar sede, etapa y contenido del internship.')
program('nvidia','NVIDIA Research Internships','https://www.nvidia.com/en-us/research/internships/',pay='unknown',eligibility='Estudiantes de posgrado e interés en áreas de investigación; requisitos por equipo.',themes='ia,metodos',priority=3)
program('openai','OpenAI Residency','https://openai.com/residency/',duration='6 meses',pay='salary',eligibility='Investigadores/builders con base técnica sólida; requisitos de dedicación según programa.',rhythm='Programa de Residency; futuras cohortes no garantizadas.',themes='ia,metodos',priority=3,watch='Confirmar sede y compatibilidad con matrícula. No es una ruta específica de ciencias sociales ni garantiza empleo posterior.')
program('anthropic','Fellows Program · AI Safety Research','https://alignment.anthropic.com/2024/anthropic-fellows-program/',pay='varies',eligibility='Perfil técnico e interés en investigación empírica de seguridad; reglas de edición.',rhythm='Fellowships documentadas; confirmar continuidad en la fuente.',themes='ia,metodos',priority=3,watch='Fuente de lanzamiento histórico: no se presupone una edición futura. Encaje CSS depende del proyecto.')

# Surveys and public sector.
for args in [
('ipsos','Ipsos','Global','UK · sedes europeas y globales','Empresa de investigación social y de mercados, encuestas y opinión.','Aprender a medir personas también es data science.','Diseño de encuestas, análisis y comunicación de resultados.','Clientes y entregables pueden limitar autoría y libertad académica.','Más medición social que una consultora tecnológica; menos autonomía científica que GESIS.','https://www.ipsos.com/en-uk/future-talent-ipsos-graduate-and-apprenticeship-opportunities'),
('kantar','Kantar','Global','Según país y programa','Empresa de investigación de mercados y análisis de comportamiento.','Útil para métodos, muestreo y conducta; elige función analítica.','Datos, medición y contacto con decisiones de clientes.','Un puesto de gestión comercial puede aportar poca investigación.','Más mercado/consumo que NatCen; distinta de una RA académica.','https://careers.kantar.com/opportunities/early-careers'),
('natcen','NatCen · National Centre for Social Research','Reino Unido','Londres · por equipo','Organización británica de investigación social, encuestas y evaluación.','Muy buen radar para métodos sociales y evidencia de política pública.','Preguntas sociales, medición y evaluación.','No consta en este atlas un graduate scheme fijo verificado.','Más investigación social/pública que Kantar; buen diálogo con LSE Methodology.','https://natcen.ac.uk/'),
('civil','UK Civil Service · analytical professions','Reino Unido','Destinos en Reino Unido','Carreras públicas de investigación social, estadística, economía e investigación operativa.','Gran escuela de policy cuantitativa; considera el compromiso y las reglas de acceso.','Problemas reales de gobierno y formación profesional.','Nacionalidad, inmigración, formación y destino pueden limitar acceso.','Más carrera pública que predoc; menos control sobre tema y publicación que una RA.','https://www.civil-service-careers.gov.uk/fast-stream/fs-all-schemes/'),
('boe','Bank of England','Reino Unido','Londres · según programa','El banco central británico, con economistas e investigación en política financiera.','Interesante para economía/datos en Londres; no para cualquier tema social.','Política cuantitativa y trabajo con economistas.','La vía de summer internship está enfocada a estudiantes de grado.','Comparador local de BCE/BIS; separa graduate, grado y PhD.','https://www.bankofengland.co.uk/careers/future-talent/graduate-programme'),
('bdf','Banque de France','Francia','París · otras sedes','Banco central francés con economía, estadísticas y análisis.','Vía posible para datos económicos si consigues un proyecto sustantivo.','Economía aplicada e infraestructura de datos.','Convenio universitario e idiomas; contenido del puesto variable.','Comparable a otros bancos centrales por tema; menos transversal que OCDE.','https://www.recrutement.banque-france.fr/fr/stages-alternance/les-stages-la-banque-de-france'),
('ukri','UKRI · Policy Internships','Reino Unido','Organizaciones de policy en UK','Esquema de estancias que conecta investigación doctoral financiada por UKRI y política pública.','Guárdalo para después de entrar al PhD, si tu financiación encaja.','Experiencia de policy vinculada al doctorado.','Requiere financiación doctoral UKRI elegible.','Más breve y policy que una RA; no prepara el acceso previo al PhD.','https://www.ukri.org/what-we-do/developing-people-and-skills/research-skills-initiatives/apprenticeships-internships-and-placements/ukri-policy-internships/')]:
    id,name,country,city,intro,verdict,upside,downside,comp,url=args
    institution(id,name,'datos',country,city,intro,verdict,upside,downside,comp,url)
program('ipsos','Generation Ipsos','https://www.ipsos.com/en-uk/generation-ipsos',duration='Según país',pay='salary',eligibility='Graduados; perfil y derecho a trabajar según país/puesto.',rhythm='Graduate programme con vías nacionales.',themes='metodos,desigualdad',priority=3,fit='Útil si aprendes diseño, medición y análisis; para el PhD tendrás que mostrar aporte metodológico propio.')
program('kantar','Graduate Programmes','https://careers.kantar.com/opportunities/early-careers',duration='Habitualmente 12–24 meses según país',pay='salary',eligibility='Graduados; requisitos según lugar y programa.',rhythm='Programas por país, no un calendario global único.',themes='metodos,plataformas',priority=3)
program('natcen','Researcher / methods / evaluation · por equipo','https://natcen.ac.uk/',kind='canal',pay='unknown',themes='metodos,causalidad,desigualdad',priority=2)
for name,themes in [('Government Social Research','metodos,desigualdad'),('Government Statistical Service','metodos'),('Government Economic Service','causalidad,macro'),('Government Operational Research Service','metodos,causalidad')]:
    program('civil',name+' · Fast Stream','https://www.civil-service-careers.gov.uk/fast-stream/fs-all-schemes/',duration='Según scheme',pay='salary',eligibility='Título con contenidos exigidos por cada profesión; Civil Service Nationality Rules e inmigración.',rhythm='Selección anual; schemes pueden cambiar.',themes=themes,priority=3,watch='La elegibilidad del GSR depende de contenidos de métodos sociales, no sólo del nombre del máster. Verificar cada scheme.')
program('boe','Graduate Development Programme','https://www.bankofengland.co.uk/careers/future-talent/graduate-programme',pay='salary',eligibility='Graduados según vía; formación y derecho a trabajar por programa.',rhythm='Cohortes.',themes='macro,metodos',priority=3)
program('boe','Summer Internships','https://www.bankofengland.co.uk/careers/future-talent/internships',stage='grado',pay='unknown',eligibility='Habitualmente penúltimo o último año de grado según el programa consultado.',rhythm='Verano.',themes='macro,metodos',priority=4,watch='No asumir elegibilidad de máster por el término internship.')
program('boe','PhD Internships','https://www.bankofengland.co.uk/careers/future-talent/phds',stage='phd',pay='unknown',eligibility='Estudiantes de PhD con investigación relevante.',rhythm='Programa doctoral.',themes='macro,metodos',priority=4)
program('bdf','Stages conventionnés','https://www.recrutement.banque-france.fr/fr/stages-alternance/les-stages-la-banque-de-france',pay='unknown',eligibility='Convenio de prácticas y perfil según departamento.',rhythm='Acoge estudiantes cada año; contratación por necesidades.',themes='macro,metodos',priority=3)
program('ukri','Policy Internships Scheme',institutions[-1]['url'],stage='phd',duration='3 meses',pay='varies',eligibility='Doctorandos con financiación UKRI elegible y permiso de supervisor.',rhythm='Rondas del esquema.',themes='metodos,ia,causalidad',priority=4)

from expand_catalogue import extend
extend(institution, program, institutions, programs)

groups=[
dict(id='investigacion',name='Los que te enseñan a investigar',short='RA & predoc',tag='Hipótesis · métodos · referencias',lead='LSE / IFS, J-PAL y Max Planck',text='Para preparar el PhD, esta sería mi primera familia. Una persona que haya visto cómo investigas puede escribir una carta mucho más concreta. Mira quién supervisa y qué producirás.',comparison='LSE/IFS para economía empírica en Londres; J-PAL para causalidad; MPIDR y GESIS para población o métodos sociales.',color='#d1ddae'),
dict(id='multilateral',name='Los que hablan con gobiernos',short='Multilaterales',tag='Desarrollo · empleo · sociedad',lead='OCDE y Banco Mundial / DIME',text='Las siglas pesan en policy, pero hay un mundo entre analizar desigualdad y organizar una agenda. Para tu cruce de IA, economía y sociedad, OCDE y DIME son mis primeras apuestas.',comparison='OCDE para comparar políticas y países; DIME para evaluarlas. ILO/UNICEF/UNU-WIDER cuando el tema sea trabajo, infancia o desarrollo.',color='#e98781'),
dict(id='economia',name='Los que mueven el dinero',short='Bancos & economía',tag='Macro · finanzas · proyectos',lead='FMI, BCE y BIS',text='Aquí hay rigor y nombres reconocidos por economistas. Si tu tesis es macrofinanciera, fantástico. Si estudias algoritmos y desigualdad, no fuerces el encaje por coleccionar un logo.',comparison='FMI/BCE/BIS para macro y estadística; bancos de desarrollo para proyectos, evaluación y desigualdad.',color='#edc968'),
dict(id='europa',name='Los que cocinan la política europea',short='Instituciones UE',tag='Ciencia · regulación · indicadores',lead='JRC, Eurofound y Cedefop',text='Blue Book abre la puerta al sistema. Para investigar, yo empezaría por JRC; para trabajo y habilidades, Eurofound y Cedefop tienen un encaje que merece mucha más atención.',comparison='JRC hace ciencia para policy. Eurofound y Cedefop profundizan en trabajo. Parlamento/Consejo acercan al proceso político.',color='#a8c8db'),
dict(id='policy',name='Los que convierten evidencia en decisiones',short='Think tanks & IA',tag='Ideas · evaluación · gobernanza',lead='GovAI, ODI Global y centros temáticos',text='Hay centros con mucha investigación y otros con más agenda pública. Para IA y sociedad, GovAI o Ada pueden encajar mejor que una marca diplomática famosa. La función exacta es decisiva.',comparison='GovAI para gobernanza de IA; ODI para policy en gobiernos; Bruegel/CEPS para Europa; Chatham/SIPRI para asuntos internacionales.',color='#d5b4d4'),
dict(id='tecnologia',name='Los que tienen los modelos y las plataformas',short='Research en empresas',tag='ML · mercados · comportamiento',lead='Microsoft Research y Google Research / DeepMind',text='Mi jugada menos obvia: el predoc Economics and Computation de MSR está pensado también para CSS. Un internship técnico brillante aporta métodos; para tu PhD necesita una pregunta social.',comparison='MSR Economics and Computation es la vía predoc más explícita de esta selección. Google amplía equipos; Amazon/Meta/Spotify interesan según experimento y datos.',color='#f0b17d'),
dict(id='datos',name='Los que saben medir a la gente',short='Encuestas & sector público',tag='Muestreo · medición · evaluación',lead='NatCen, GESIS y profesiones analíticas',text='No todo es una red neuronal. Si no sabes cómo se midió una variable social, puedes modelizar muy bien un problema mal definido. Encuestas, estadística pública y evaluación tienen muchísimo que aportar.',comparison='NatCen para investigación social, Ipsos/Kantar para medición aplicada; Fast Stream para carrera pública cuantitativa.',color='#b8d3cb')]

voices=[
dict(name='J-PAL · dos reseñas de internships',type='Reseñas independientes · muestra de 2',date='2017 y 2021',up='Destacan colaboración y variedad de tareas.',down='Una reseña describe mucha carga; otra advierte de tareas administrativas.',limit='No son una muestra representativa, ni las mismas sedes, ni el mismo puesto que una Data RA actual.',url='https://app.joinhandshake.com/employers/abdul-latif-jameel-poverty-action-lab-j-pal-18136/reviews'),
dict(name='ONU · Fair Internship Initiative',type='Encuestas de una organización de defensa de interns',date='Informes 2017 / índice 2023',up='Ofrece una perspectiva que no depende del marketing de cada organismo.',down='Señala barreras económicas y desigualdad de acceso por prácticas sin pago o con apoyo insuficiente.',limit='Informes históricos, participantes autoseleccionados y organismos heterogéneos. No trasladar un resultado a toda la ONU ni usarlo como dato actual de una agencia.',url='https://fairinternshipinitiative.wordpress.com/our-reports/'),
dict(name='Blue Book / Schuman · conversación pública',type='Foro anónimo · experiencia de candidatura',date='Conversación consultada en septiembre de 2026',up='Los participantes valoran la experiencia institucional y proponen vías profesionales paralelas.',down='La persona que abre el hilo expresa cansancio por rechazos y encadenar prácticas.',limit='Relato individual sin identidad ni experiencia verificadas. No mide tasa de admisión, satisfacción ni calidad de supervisión.',url='https://www.reddit.com/r/EUCareers/comments/1uqqc2h/is_applying_to_the_schuman_or_blue_book/'),
dict(name='Microsoft Research · EuroSys',type='Testimonios personales publicados por una comunidad académica',date='Testimonios históricos',up='Describen colaboración, aprendizaje investigador y trabajo que puede desembocar en artículos.',down='No ofrecen una evaluación sistemática de problemas ni condiciones actuales.',limit='Experiencias de PhD en grupos de sistemas, no del predoc económico; no permiten comparar todas las empresas.',url='https://www.eurosys.org/eurosys-for-students/testimonials'),
dict(name='Banco Mundial · antiguos interns',type='Testimonios seleccionados por la institución',date='Página consultada 30/09/2026',up='Un participante describe encuestas, entrevistas y evaluación en IFC; otros destacan aprendizaje y contactos.',down='La página no ofrece una muestra de críticas ni tasas de satisfacción.',limit='Fuente institucional promocional. Los testimonios son ejemplos de tareas, no un balance representativo del programa.',url='https://www.worldbank.org/ext/en/careers/talent-programs/wbg-pioneers'),
dict(name='J-PAL Africa · Research Associates',type='Testimonios seleccionados por la institución',date='Página consultada 30/09/2026',up='Describen aprendizaje más allá del puesto y trabajo con evaluaciones.',down='No hay una muestra comparable de experiencias negativas en esa página.',limit='Útil para entender el tipo de trabajo; no demuestra que todos los proyectos tengan la misma supervisión.',url='https://www.povertyactionlab.org/j-pal-africa-working-j-pal-africa'),
dict(name='EEA · experiencia de trainees',type='Testimonios seleccionados por la agencia',date='Página consultada 30/09/2026',up='Describen trabajo entre evidencia científica y política ambiental.',down='La selección institucional no permite medir problemas recurrentes.',limit='No generalizar de una experiencia positiva a todas las unidades ni a una futura edición.',url='https://www.eea.europa.eu/en/about/careers/traineeships'),
dict(name='Eurofound · Social Policies trainee',type='Experiencia publicada por la institución',date='Página consultada 30/09/2026',up='La agencia ofrece un relato del trabajo en investigación de política social.',down='Una experiencia ilustrativa no revela distribución de satisfacción ni calidad de todos los equipos.',limit='Fuente promocional; sirve para explorar tareas y contexto, no para construir un ranking de experiencia laboral.',url='https://www.eurofound.europa.eu/en/pages/vacancies/information-on-traineeships')]

themes=dict(ia='IA & trabajo',causalidad='Política & causalidad',desigualdad='Desigualdad',plataformas='Plataformas & redes',metodos='Métodos & encuestas',clima='Clima & territorio',salud='Salud & población',macro='Macro & finanzas')
targets=[dict(name='Oxford · DPhil Social Data Science',url='https://www.ox.ac.uk/admissions/graduate/courses/dphil-social-data-science'),dict(name='LSE · MPhil/PhD Computational Social Science',url='https://www.lse.ac.uk/study-at-lse/graduate/mphilphd-computational-social-science')]
data=dict(title='Social Data Club',reviewed='2026-09-30',institutions=institutions,programs=programs,groups=groups,themes=themes,voices=voices,targets=targets)
out=ROOT/'dist'; out.mkdir(exist_ok=True)
(ROOT/'data').mkdir(exist_ok=True)
(ROOT/'data/catalogue.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(out/'catalogue.js').write_text('window.ATLAS = '+json.dumps(data,ensure_ascii=False,separators=(',',':'))+';\n')
urls=sorted(set([i['url'] for i in institutions]+[i['portal'] for i in institutions if i.get('portal')]+[p['url'] for p in programs]+[v['url'] for v in voices]+[t['url'] for t in targets]))
(out/'fuentes.txt').write_text('SOCIAL DATA CLUB · fuentes enlazadas · corte 30/09/2026\nResumen editorial original; los documentos de terceros conservan sus derechos.\nNo implica lectura íntegra de cada documento ni disponibilidad de plazas.\n\n'+'\n'.join(urls)+'\n')
print(f'{len(institutions)} instituciones · {len(programs)} rutas · {sum(p["kind"]=="programa" for p in programs)} programas · {len(urls)} fuentes enlazadas')
