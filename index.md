<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
<style>
:root {
  --primary: #1B3A6B;
  --text: #1f2937;
  --muted: #6b7280;
  --border: #e5e7eb;
  --soft: #f8fafc;
  --white: #ffffff;
}

.site-wrapper {
  max-width: 1050px;
  margin: 0 auto;
  padding: 10px 22px 60px;
  color: var(--text);
}

.site-nav {
  position: sticky;
  top: 0;
  z-index: 20;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  padding: 16px 0;
  margin-bottom: 36px;
  background: rgba(255,255,255,.96);
  border-bottom: 1px solid var(--border);
  backdrop-filter: blur(8px);
}

.site-brand {
  color: var(--text) !important;
  text-decoration: none !important;
  font-size: 1.15rem;
  font-weight: 750;
  white-space: nowrap;
}

.site-links {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-end;
  gap: 8px 18px;
}

.site-links a {
  color: #4b5563 !important;
  text-decoration: none !important;
  font-size: .92rem;
}

.site-links a:hover { color: var(--primary) !important; }

.page-section { display: block; }

/* Quand une section est ciblée, elle devient la seule section visible. */
body:has(.page-section:target) .page-section { display: none; }
body:has(.page-section:target) .page-section:target { display: block; }

.hero {
  padding: 34px 0 48px;
  border-bottom: 1px solid var(--border);
}

.eyebrow {
  margin: 0 0 10px;
  color: var(--primary);
  font-size: .88rem;
  font-weight: 700;
  letter-spacing: .04em;
  text-transform: uppercase;
}

.hero h1 {
  margin: 0;
  font-size: clamp(2.4rem, 6vw, 4.4rem);
  line-height: 1;
  letter-spacing: -.045em;
}

.hero h2 {
  margin: 16px 0 12px;
  font-size: clamp(1.25rem, 3vw, 1.75rem);
  font-weight: 500;
  color: #4b5563;
}

.lead {
  max-width: 760px;
  margin: 18px 0 0;
  font-size: 1.08rem;
  line-height: 1.8;
}

.meta-line { margin: 10px 0 0; color: var(--muted); }

.socials {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  margin-top: 22px;
}

.socials a { text-decoration: none; }

.cv-button {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  margin-top: 20px;
  padding: 10px 15px;
  border-radius: 7px;
  background: var(--primary);
  color: white !important;
  text-decoration: none !important;
  font-weight: 650;
}

.section-inner {
  padding: 44px 0 20px;
}

.section-inner h1 {
  margin: 0 0 12px;
  font-size: clamp(2rem, 5vw, 3rem);
  letter-spacing: -.03em;
}

.section-inner h2 {
  margin: 42px 0 14px;
  padding-top: 0;
  border-top: 0;
  font-size: 1.45rem;
}

.section-inner h3 {
  margin-top: 30px;
  font-size: 1.12rem;
}

.section-inner p,
.section-inner li {
  line-height: 1.75;
}

.section-inner a { color: var(--primary); }

.about-grid {
  display: grid;
  grid-template-columns: minmax(0, 1.55fr) minmax(230px, .75fr);
  gap: 42px;
  align-items: start;
  margin-top: 28px;
}

.profile-photo {
  width: 100%;
  max-width: 300px;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  border-radius: 14px;
  display: block;
  margin-left: auto;
  border: 1px solid var(--border);
}

.profile-card {
  padding: 22px;
  background: var(--soft);
  border: 1px solid var(--border);
  border-radius: 12px;
}

.profile-card h2 { margin-top: 0; }

.skill-block { margin: 26px 0; }
.skill-block p { margin: 6px 0; }

.project {
  padding: 24px 0;
  border-bottom: 1px solid var(--border);
}

.project:first-of-type { padding-top: 8px; }
.project h2 { margin: 0 0 6px; font-size: 1.3rem; }
.project-type { margin: 0 0 10px; color: var(--muted); font-weight: 600; }
.project p { margin: 8px 0; }

.cert-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin-top: 22px;
}

.cert-card {
  padding: 18px;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: var(--white);
}

.cert-card strong { display: block; margin-bottom: 6px; }
.cert-card span { color: var(--muted); font-size: .94rem; }
.cert-card a { display: inline-block; margin-top: 9px; }

.edu-item {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin: 22px 0;
  padding-bottom: 22px;
  border-bottom: 1px solid var(--border);
}

.edu-logo {
  width: 62px;
  height: 62px;
  object-fit: contain;
  flex: 0 0 62px;
  border-radius: 8px;
}

.contact-list p { margin: 8px 0; }

@media (max-width: 760px) {
  .site-nav { position: static; align-items: flex-start; flex-direction: column; }
  .site-links { justify-content: flex-start; }
  .about-grid { grid-template-columns: 1fr; }
  .profile-photo { margin: 0; max-width: 260px; }
  .cert-grid { grid-template-columns: 1fr; }
}
</style>
<div class="site-wrapper">
<nav class="site-nav">
  <a class="site-brand" href="#accueil">Fabrice BOMISSO</a>
  <div class="site-links">
    <a href="#a-propos">À propos</a>
    <a href="#competences">Compétences</a>
    <a href="#projets">Projets</a>
    <a href="#recherche">Recherche</a>
    <a href="#experience">Expérience</a>
    <a href="#formation">Formation</a>
    <a href="#certifications">Certifications</a>
    <a href="#contact">Contact</a>
  </div>
</nav>
<section id="accueil" class="page-section hero">
  <p class="eyebrow">Data Analyst · Business Intelligence · Data Science</p>
  <h1>Fabrice BOMISSO</h1>
  <h2>Data Analyst | Business Intelligence | Data Science</h2>
  <p class="meta-line">Abidjan, Côte d'Ivoire</p>
  <p class="lead">Je transforme les données en informations fiables et exploitables pour faciliter la prise de décision.</p>
  <p class="lead">Mon travail porte principalement sur la <strong>Business Intelligence</strong>, la <strong>Data Analytics</strong> et le <strong>Machine Learning</strong>, avec une attention particulière portée à la qualité des données, à la modélisation et à l'interprétation des résultats.</p>
  <div class="socials">
    <a href="tel:+2250545778538">(+225) 05 45 77 85 38</a>
    <a href="tel:+2250778314526">07 78 31 45 26</a>
    <a href="mailto:fabricebtibo@mail.com">fabricebtibo@mail.com</a>
    <a href="mailto:fabricebtibo@yahoo.com">fabricebtibo@yahoo.com</a>
    <a href="https://www.linkedin.com/in/fabrice-bomisso/" target="_blank" rel="noopener noreferrer"><i class="fab fa-linkedin"></i> LinkedIn</a>
    <a href="https://github.com/fbomisso/fabrice.bomisso/" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i> GitHub</a>
  </div>
  <a class="cv-button" href="./documents/CV_Fabrice_Bomisso.pdf"><i class="fas fa-file-pdf"></i> Télécharger mon CV</a>
</section>
<section id="a-propos" class="page-section section-inner">
  <h1>À propos</h1>
  <div class="about-grid">
    <div>
      <h2>👋 À propos de moi</h2>
      <p>Je travaille sur des problématiques d'analyse de données, de Business Intelligence et de Machine Learning.</p>
      <p>Je m'intéresse particulièrement à la qualité des données, à la modélisation, à la construction d'indicateurs fiables et à la transformation des résultats d'analyse en éléments utiles à la décision.</p>
      <h2>🧑‍💻 Profil professionnel</h2>
      <p>Mon approche combine analyse, modélisation et visualisation afin de transformer des données brutes en informations fiables, compréhensibles et exploitables par les décideurs.</p>
      <p>Je porte une attention particulière à la qualité des données, à la validation des indicateurs, à la cohérence des modèles et à l'interprétation des résultats.</p>
      <h2>🧭 Ma démarche</h2>
      <p><strong>Données → Audit → Nettoyage → Transformation → Modélisation → Analyse → Visualisation → Insights → Recommandations</strong></p>
      <p>Je cherche à aller au-delà de la simple production de graphiques : comprendre le problème, fiabiliser la donnée, construire des indicateurs cohérents et produire des analyses utiles à la décision.</p>
    </div>
    <div>
      <img class="profile-photo" src="./img/photo.jpeg" alt="Fabrice BOMISSO">
      <div class="profile-card" style="margin-top:18px;">
        <h2>🧰 Outils et technologies</h2>
        <p><strong>Business Intelligence</strong><br>Power BI, Power Query, DAX, Data Modeling, Data Visualization, Excel</p>
        <p><strong>Data Analytics</strong><br>Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook</p>
        <p><strong>Machine Learning</strong><br>Scikit-learn, Random Forest, SHAP, Streamlit</p>
        <p><strong>Bases de données</strong><br>SQL, SQL Server</p>
        <p><strong>Environnement</strong><br>Git, GitHub, VS Code</p>
      </div>
    </div>
  </div>
</section>
<section id="competences" class="page-section section-inner">
  <h1>Compétences</h1>
  <div class="skill-block">
    <h2>Business Intelligence</h2>
    <p><strong>Power BI, Power Query, DAX, Data Modeling, Data Visualization, Excel</strong></p>
    <ul><li>Modélisation en étoile et en constellation</li><li>Transformation et nettoyage des données</li><li>Création de KPI et mesures DAX</li><li>Audit et contrôle de la qualité des données</li><li>Analyse de performance et reporting décisionnel</li><li>Data storytelling</li></ul>
  </div>
  <div class="skill-block">
    <h2>Data Analytics et Python</h2>
    <p><strong>Python, Pandas, NumPy, Matplotlib, Seaborn</strong></p>
    <ul><li>Exploration et analyse de données</li><li>Nettoyage et préparation des données</li><li>Analyse statistique</li><li>Feature Engineering</li><li>Visualisation de données</li></ul>
  </div>
  <div class="skill-block">
    <h2>Machine Learning</h2>
    <p><strong>Scikit-learn, Random Forest, SHAP, Streamlit</strong></p>
    <ul><li>Classification</li><li>Évaluation des modèles</li><li>Analyse des variables importantes</li><li>Explainability</li><li>Segmentation des risques</li><li>Déploiement d'applications de prédiction</li></ul>
  </div>
  <div class="skill-block">
    <h2>Outils</h2>
    <h3>Data Analysis & Python</h3><p>Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook</p>
    <h3>Business Intelligence</h3><p>Power BI, Power Query, DAX, Excel</p>
    <h3>Data Science & Machine Learning</h3><p>Scikit-learn, SHAP, Streamlit</p>
    <h3>Data Profiling & Exploration</h3><p>ydata-profiling, Sweetviz, Lux</p>
    <h3>Bases de données & SQL</h3><p>SQL, SQL Server</p>
    <h3>Développement & environnement</h3><p>Git, GitHub, VS Code</p>
  </div>
</section>
<section id="projets" class="page-section section-inner">
  <h1>Projets</h1>
  <p>Une sélection de projets réalisés en Business Intelligence, Data Analytics et Data Science.</p>

  <div class="project"><h2>01. Customer Churn Prediction</h2><p class="project-type">Machine Learning · Telco</p><p>Prédiction du risque de churn client avec Random Forest, analyse SHAP, segmentation des risques et application Streamlit.</p><p><strong>Résultats :</strong> Recall 77,81 % · F1-score 63,75 % · ROC-AUC 0,85</p><a href="./Machine-Learning/Classification/Customer-Churn-Prediction/">Voir le projet</a></div>
  <div class="project"><h2>02. Retail Analytics</h2><p class="project-type">Power BI · Data Quality · DAX</p><p>Analyse retail basée sur un modèle en étoile, avec audit des indicateurs, diagnostic de bugs DAX et validation des résultats.</p><a href="./PowerBI/analyse-retail-star-schema/">Voir le projet</a></div>
  <div class="project"><h2>03. Olist E-commerce Analytics</h2><p class="project-type">Power BI · E-commerce · Data Modeling</p><p>Analyse d'une marketplace e-commerce brésilienne avec modélisation en constellation, contrôle des différents grains de données et analyse de la performance logistique.</p><a href="./PowerBI/analyse-performance-olist/">Voir le projet</a></div>
  <div class="project"><h2>04. PitchSide Pro Revenue</h2><p class="project-type">Power BI · Revenue Analytics · Business Intelligence</p><p>Analyse de la croissance des revenus d'une plateforme e-commerce spécialisée dans les articles de football, avec décomposition du revenu entre trafic, conversion et panier moyen.</p><a href="./PowerBI/analyse-pitchside-pro-revenue/">Voir le projet</a></div>
  <div class="project"><h2>05. Performance Football Européen</h2><p class="project-type">Power BI · Sport Analytics · Scouting</p><p>Analyse de la performance des joueurs et des équipes du football européen, avec des volets consacrés au scouting, aux statistiques, à la valorisation et aux effectifs.</p><a href="./PowerBI/analyse-performance-football-europe/">Voir le projet</a></div>
  <div class="project"><h2>06. GAP_SERVICE</h2><p class="project-type">Power BI · Data Analytics · Data Quality</p><a href="./PowerBI/GAP_SERVICE/">Voir le projet</a></div>
  <div class="project"><h2>07. Pilotage Décisionnel d'un Réseau de Distribution Multi-Magasins avec Power BI</h2><p class="project-type">Power BI · Business Intelligence · Pilotage décisionnel</p><a href="./PowerBI/Pilotage%20D%C3%A9cisionnel%20d%27un%20R%C3%A9seau%20de%20Distribution%20Multi-Magasins%20avec%20Power%20BI/">Voir le projet</a></div>
  <p><strong>Tous mes projets</strong></p>
  <p><a href="./PowerBI/">Voir mes projets Power BI</a></p>
  <p><a href="./Machine-Learning/">Voir mes projets Machine Learning</a></p>
</section>
<section id="recherche" class="page-section section-inner">
  <h1>Recherche et travaux académiques</h1>
  <h2>Diagnostic de la défécation à l'air libre dans le district de Yamoussoukro</h2>
  <p><strong>Recherche appliquée · Eau, Assainissement et Environnement · Analyse de données</strong></p>
  <p>Travail de recherche consacré au diagnostic de la défécation à l'air libre dans le district de Yamoussoukro et à l'identification des principaux facteurs associés à cette pratique.</p>
  <h3>Méthodologie :</h3>
  <ul><li>Enquête auprès de 373 ménages</li><li>Collecte de données sur le terrain</li><li>Entretiens semi-structurés</li><li>Observations directes</li><li>Analyse de données socio-économiques et sanitaires</li><li>Traitement et interprétation des résultats</li></ul>
  <h3>Principaux axes d'analyse :</h3>
  <ul><li>Accès aux infrastructures d'assainissement</li><li>Pratiques de défécation à l'air libre</li><li>Facteurs économiques, sociaux et culturels</li><li>Niveau d'éducation et pratiques sanitaires</li><li>Identification des leviers d'intervention</li><li>Proposition de stratégies adaptées au contexte local</li></ul>
  <p><strong>Publication :</strong> World Journal of Advanced Research and Reviews, 2024, 24(1), 1119-1125</p>
  <p><strong>Auteurs :</strong> Kinanpara KONE, Yao Francis KOUAME, Tibo Fabrice BOMISSO, Jean Renaud ALLOUKO et Kotchi Yves BONY</p>
  <p><a href="https://wjarr.com/content/diagnosis-open-defecation-yamoussoukro-district-central-cote-divoire" target="_blank" rel="noopener noreferrer">Lire la publication</a></p>
</section>
<section id="experience" class="page-section section-inner">
  <h1>Expérience</h1>
  <h2>Groupe Inova, Abidjan</h2>
  <p><strong>Avril 2025 à Juillet 2026</strong></p>
  <ul><li>Nettoyage, contrôle et préparation de données collectées par web scraping.</li><li>Participation à la structuration et à l'alimentation de la base de données de l'application web.</li><li>Contrôle de la qualité et de la cohérence des données avant intégration.</li><li>Participation au développement d'une plateforme de visualisation.</li></ul>
</section>
<section id="formation" class="page-section section-inner">
  <h1>Formation</h1>
  <div class="edu-item"><img class="edu-logo" src="./img/logos/fatala.fr.png" alt="Logo Fatala Digital House"><div><h2 style="margin:0 0 5px;">Data Science et IA, Bootcamp</h2><strong>Fatala Digital House, en cours</strong><p>Formation pratique en Data Science, Machine Learning et Intelligence Artificielle, avec un parcours axé sur Python, analyse de données, Machine Learning et réalisation de projets.</p><a href="https://academy.fatala.fr/" target="_blank" rel="noopener noreferrer">Fatala Digital House</a></div></div>
  <div class="edu-item"><img class="edu-logo" src="./img/logos/Gomycode.webp" alt="Logo GOMYCODE"><div><h2 style="margin:0 0 5px;">Data Analyst</h2><strong>GOMYCODE, Novembre 2024 à Mars 2025</strong><p>Formation orientée Data Analytics, Python, analyse de données et outils décisionnels.</p><a href="https://gomycode.com/ic/fr/" target="_blank" rel="noopener noreferrer">GOMYCODE</a></div></div>
  <div class="edu-item"><img class="edu-logo" src="./img/logos/Universite-Jean-Lorougnon-Guede250-1.png" alt="Logo Université Jean Lorougnon Guédé"><div><h2 style="margin:0 0 5px;">Master, Génie de l'Eau et de l'Environnement</h2><a href="https://ujlog.edu.ci/" target="_blank" rel="noopener noreferrer"><strong>Université Jean Lorougnon Guédé</strong></a><p>Daloa, Côte d'Ivoire</p></div></div>
  <div class="edu-item"><img class="edu-logo" src="./img/logos/Universite-Jean-Lorougnon-Guede250-1.png" alt="Logo Université Jean Lorougnon Guédé"><div><h2 style="margin:0 0 5px;">Licence, Génie de l'Eau et de l'Environnement</h2><a href="https://ujlog.edu.ci/" target="_blank" rel="noopener noreferrer"><strong>Université Jean Lorougnon Guédé</strong></a><p>Daloa, Côte d'Ivoire</p></div></div>
</section>
<section id="certifications" class="page-section section-inner">
  <h1>Certifications</h1>
  <div class="cert-grid">
    <div class="cert-card"><strong><i class="fas fa-chart-line"></i> Data Analyst | GOMYCODE</strong><span>Microsoft Power BI · Certificat de réussite</span><br><a href="./certifications/BOMISSO%20TIBO%20FABRICE-Data%20Analytics%20-%20Microsoft%20Power%20BI%20Certified_%20Certificate%20of%20Completion.pdf"><i class="fas fa-file-pdf"></i> Voir le certificat</a></div>
    <div class="cert-card"><strong><i class="fas fa-project-diagram"></i> Gestion de projet</strong><span>Certificat de formation</span><br><a href="./certifications/Certificat%20GESTION%20DE%20PROJET.pdf"><i class="fas fa-file-pdf"></i> Voir le certificat</a></div>
    <div class="cert-card"><strong><i class="fas fa-chart-pie"></i> MEAL</strong><span>Certificat MEAL</span><br><a href="./certifications/Certificat%20MEAL.pdf"><i class="fas fa-file-pdf"></i> Voir le certificat</a></div>
    <div class="cert-card"><strong><i class="fas fa-tint"></i> WASH dans les situations d'urgence</strong><span>Certificat de formation</span><br><a href="./certifications/Certificat%20WASH%20dans%20les%20situations%20d'urgence.pdf"><i class="fas fa-file-pdf"></i> Voir le certificat</a></div>
    <div class="cert-card"><strong><i class="fas fa-shield-alt"></i> HSE</strong><span>Certificat HSE</span><br><a href="./certifications/Certificat%20HSE.pdf"><i class="fas fa-file-pdf"></i> Voir le certificat</a></div>
    <div class="cert-card"><strong><i class="fas fa-file-alt"></i> Rédaction d'article scientifique</strong><span>World Journal of Advanced Research and Reviews · 2024</span><br><a href="./certifications/Certifact%20redaction%20d'article%20scientifique.pdf" target="_blank" rel="noopener noreferrer"><i class="fas fa-file-pdf"></i> Voir le certificat</a><br><a href="https://wjarr.com/content/diagnosis-open-defecation-yamoussoukro-district-central-cote-divoire" target="_blank" rel="noopener noreferrer"><i class="fas fa-external-link-alt"></i> Lire la publication</a></div>
  </div>
</section>
<section id="contact" class="page-section section-inner">
  <h1>Contact</h1>
  <p>Pour une opportunité, une collaboration ou un échange autour de la Data, vous pouvez me contacter directement.</p>
  <div class="contact-list">
    <p>📧 <a href="mailto:fabricebtibo@mail.com">fabricebtibo@mail.com</a></p>
    <p>📧 <a href="mailto:fabricebtibo@yahoo.com">fabricebtibo@yahoo.com</a></p>
    <p>📞 <a href="tel:+2250545778538">(+225) 05 45 77 85 38</a></p>
    <p>📞 <a href="tel:+2250778314526">07 78 31 45 26</a></p>
    <p><a href="https://www.linkedin.com/in/fabrice-bomisso/" target="_blank" rel="noopener noreferrer"><i class="fab fa-linkedin"></i> linkedin.com/in/fabrice-bomisso</a></p>
    <p><a href="https://github.com/fbomisso/fabrice.bomisso/" target="_blank" rel="noopener noreferrer"><i class="fab fa-github"></i> github.com/fbomisso/fabrice.bomisso</a></p>
  </div>
  <a class="cv-button" href="./documents/CV_Fabrice_Bomisso.pdf"><i class="fas fa-file-pdf"></i> Télécharger mon CV</a>
</section>
</div>
