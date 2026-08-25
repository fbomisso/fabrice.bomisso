<style>
/* =========================================================
   FABRICE BOMISSO — portfolio
   Navigation inspired by clean Hugo / PaperMod portfolios
   ========================================================= */

:root {
  --portfolio-text: #1f2937;
  --portfolio-muted: #6b7280;
  --portfolio-border: #e5e7eb;
  --portfolio-link: #2563eb;
  --portfolio-card: #ffffff;
  --portfolio-bg: #ffffff;
}

html { scroll-behavior: smooth; }

body {
  background: var(--portfolio-bg);
  color: var(--portfolio-text);
}

.portfolio-shell {
  max-width: 980px;
  margin: 0 auto;
  padding: 0 24px 60px;
  color: var(--portfolio-text);
}

.portfolio-nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 28px;
  padding: 18px 0 22px;
  margin-bottom: 54px;
  border-bottom: 1px solid var(--portfolio-border);
}

.portfolio-brand {
  flex: 0 0 auto;
  color: var(--portfolio-text) !important;
  text-decoration: none !important;
  font-size: 1.12rem;
  font-weight: 700;
  letter-spacing: -0.02em;
}

.portfolio-nav-right {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  gap: 18px;
  min-width: 0;
}

.portfolio-links {
  display: flex;
  align-items: center;
  justify-content: flex-end;
  flex-wrap: wrap;
  gap: 16px;
}

.portfolio-links a {
  color: var(--portfolio-text) !important;
  text-decoration: none !important;
  font-size: 0.91rem;
  white-space: nowrap;
}

.portfolio-links a:hover {
  color: var(--portfolio-link) !important;
}

.theme-toggle {
  width: 34px;
  height: 34px;
  padding: 0;
  border: 1px solid var(--portfolio-border);
  border-radius: 50%;
  background: transparent;
  color: var(--portfolio-text);
  cursor: pointer;
  font-size: 16px;
  line-height: 32px;
  text-align: center;
  flex: 0 0 auto;
}

.theme-toggle:hover {
  background: var(--portfolio-border);
}

.portfolio-section {
  display: none;
  animation: portfolioFade 0.18s ease-out;
}

.portfolio-section.active {
  display: block;
}

@keyframes portfolioFade {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.portfolio-home h1 {
  margin: 0 0 8px;
  font-size: 2.7rem;
  line-height: 1.08;
  letter-spacing: -0.04em;
}

.portfolio-home .subtitle {
  margin: 0 0 18px;
  color: var(--portfolio-muted);
  font-size: 1.08rem;
}

.portfolio-home .intro {
  max-width: 760px;
  font-size: 1.05rem;
  line-height: 1.75;
}

.portfolio-section h1,
.portfolio-section h2,
.portfolio-section h3,
.portfolio-section h4 {
  color: var(--portfolio-text);
}

.portfolio-section h1 {
  margin-top: 0;
  font-size: 2.25rem;
  letter-spacing: -0.03em;
}

.portfolio-section h2 {
  margin-top: 34px;
  font-size: 1.55rem;
}

.portfolio-section h3 {
  margin-top: 28px;
  font-size: 1.15rem;
}

.portfolio-section h4 {
  margin-top: 20px;
  font-size: 1rem;
}

.portfolio-section p,
.portfolio-section li {
  line-height: 1.7;
}

.portfolio-section a {
  color: var(--portfolio-link);
}

.about-layout {
  display: grid;
  grid-template-columns: minmax(0, 1fr) 210px;
  gap: 46px;
  align-items: start;
}

.about-photo {
  width: 210px;
  height: 250px;
  object-fit: cover;
  border-radius: 14px;
  border: 1px solid var(--portfolio-border);
  display: block;
}

.meta-line {
  color: var(--portfolio-muted);
  margin-top: -8px;
}

.project-card {
  margin: 0 0 30px;
  padding: 0 0 26px;
  border-bottom: 1px solid var(--portfolio-border);
}

.project-card:last-child { border-bottom: 0; }

.project-card h3 { margin-bottom: 5px; }

.project-type {
  color: var(--portfolio-muted);
  font-size: 0.92rem;
  font-weight: 600;
}

.project-link {
  font-weight: 600;
  text-decoration: none;
}

.project-link:hover { text-decoration: underline; }

.cert-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 14px;
  margin-top: 20px;
}

.cert-card {
  border: 1px solid var(--portfolio-border);
  border-radius: 10px;
  padding: 16px;
  background: var(--portfolio-card);
}

.cert-card strong { display: block; margin-bottom: 7px; }
.cert-card span { color: var(--portfolio-muted); font-size: 0.92rem; }

.contact-line { margin: 10px 0; }

.cv-button {
  display: inline-block;
  margin-top: 16px;
  padding: 9px 14px;
  border-radius: 7px;
  background: var(--portfolio-text);
  color: var(--portfolio-bg) !important;
  text-decoration: none !important;
  font-weight: 600;
}

.cv-button:hover { opacity: 0.86; }

.portfolio-footer {
  margin-top: 60px;
  padding-top: 22px;
  border-top: 1px solid var(--portfolio-border);
  color: var(--portfolio-muted);
  font-size: 0.86rem;
}

@media (max-width: 850px) {
  .portfolio-nav {
    align-items: flex-start;
  }
  .portfolio-nav-right {
    gap: 12px;
  }
  .portfolio-links {
    gap: 10px 14px;
  }
}

@media (max-width: 680px) {
  .portfolio-shell { padding: 0 18px 40px; }
  .portfolio-nav {
    flex-direction: column;
    margin-bottom: 36px;
  }
  .portfolio-nav-right {
    width: 100%;
    justify-content: space-between;
  }
  .portfolio-links { justify-content: flex-start; }
  .portfolio-home h1 { font-size: 2.2rem; }
  .about-layout { grid-template-columns: 1fr; }
  .about-photo { width: 150px; height: 180px; }
  .cert-grid { grid-template-columns: 1fr; }
}

/* Dark mode */
body.portfolio-dark {
  --portfolio-text: #e5e7eb;
  --portfolio-muted: #9ca3af;
  --portfolio-border: #374151;
  --portfolio-link: #93c5fd;
  --portfolio-card: #111827;
  --portfolio-bg: #0b0f14;
}
</style>

<div class="portfolio-shell">

<nav class="portfolio-nav" aria-label="Navigation principale">
  <a class="portfolio-brand" href="#accueil" data-section="accueil">Fabrice Bomisso</a>
  <div class="portfolio-nav-right">
    <div class="portfolio-links">
      <a href="#a-propos" data-section="a-propos">À propos</a>
      <a href="#competences" data-section="competences">Compétences</a>
      <a href="#projets" data-section="projets">Projets</a>
      <a href="#recherche" data-section="recherche">Recherche</a>
      <a href="#experience" data-section="experience">Expérience</a>
      <a href="#formation" data-section="formation">Formation</a>
      <a href="#certifications" data-section="certifications">Certifications</a>
      <a href="#contact" data-section="contact">Contact</a>
    </div>
    <button class="theme-toggle" id="theme-toggle" type="button" aria-label="Changer le thème" title="Changer le thème">☾</button>
  </div>
</nav>

<section id="accueil" class="portfolio-section portfolio-home active">
  <h1>Fabrice BOMISSO</h1>
  <p class="subtitle">Data Analyst | Business Intelligence | Data Science</p>
  <p>Abidjan, Côte d'Ivoire</p>

  <p class="intro">Je transforme les données en informations fiables et exploitables pour faciliter la prise de décision.</p>

  <p>Mon travail porte principalement sur la <strong>Business Intelligence</strong>, la <strong>Data Analytics</strong> et le <strong>Machine Learning</strong>, avec une attention particulière portée à la qualité des données, à la modélisation et à l'interprétation des résultats.</p>

  <p>
    <a href="mailto:fabricebtibo@mail.com">Email</a> ·
    <a href="https://www.linkedin.com/in/fabrice-bomisso/" target="_blank" rel="noopener noreferrer">LinkedIn</a> ·
    <a href="https://github.com/fbomisso/fabrice.bomisso/" target="_blank" rel="noopener noreferrer">GitHub</a>
  </p>

  <a class="cv-button" href="./documents/CV_Fabrice_Bomisso.pdf">Télécharger mon CV</a>
</section>

<section id="a-propos" class="portfolio-section">
  <div class="about-layout">
    <div>
      <h1>À propos</h1>
      <p>Je travaille sur des problématiques d'analyse de données, de Business Intelligence et de Machine Learning.</p>
      <p>Je m'intéresse particulièrement à la qualité des données, à la modélisation, à la construction d'indicateurs fiables et à la transformation des résultats d'analyse en éléments utiles à la décision.</p>
      <p>Mon approche va de la donnée brute à l'interprétation :</p>
      <p><strong>Données → Audit → Nettoyage → Transformation → Modélisation → Analyse → Visualisation → Insights → Recommandations</strong></p>
    </div>
    <div>
      <img class="about-photo" src="./img/photo.jpeg" alt="Fabrice BOMISSO">
    </div>
  </div>
</section>

<section id="competences" class="portfolio-section">
  <h1>Compétences</h1>

  <h2>Business Intelligence</h2>
  <p><strong>Power BI, Power Query, DAX, Data Modeling, Data Visualization, Excel</strong></p>
  <ul>
    <li>Modélisation en étoile et en constellation</li>
    <li>Transformation et nettoyage des données</li>
    <li>Création de KPI et mesures DAX</li>
    <li>Audit et contrôle de la qualité des données</li>
    <li>Analyse de performance et reporting décisionnel</li>
    <li>Data storytelling</li>
  </ul>

  <h2>Data Analytics et Python</h2>
  <p><strong>Python, Pandas, NumPy, Matplotlib, Seaborn</strong></p>
  <ul>
    <li>Exploration et analyse de données</li>
    <li>Nettoyage et préparation des données</li>
    <li>Analyse statistique</li>
    <li>Feature Engineering</li>
    <li>Visualisation de données</li>
  </ul>

  <h2>Machine Learning</h2>
  <p><strong>Scikit-learn, Random Forest, SHAP, Streamlit</strong></p>
  <ul>
    <li>Classification</li>
    <li>Évaluation des modèles</li>
    <li>Analyse des variables importantes</li>
    <li>Explainability</li>
    <li>Segmentation des risques</li>
    <li>Déploiement d'applications de prédiction</li>
  </ul>

  <h2>Outils</h2>
  <h4>Data Analysis & Python</h4>
  <p>Python, Pandas, NumPy, Matplotlib, Seaborn, Jupyter Notebook</p>
  <h4>Business Intelligence</h4>
  <p>Power BI, Power Query, DAX, Excel</p>
  <h4>Data Science & Machine Learning</h4>
  <p>Scikit-learn, SHAP, Streamlit</p>
  <h4>Data Profiling & Exploration</h4>
  <p>ydata-profiling, Sweetviz, Lux</p>
  <h4>Bases de données & SQL</h4>
  <p>SQL, SQL Server</p>
  <h4>Développement & environnement</h4>
  <p>Git, GitHub, VS Code</p>
</section>

<section id="projets" class="portfolio-section">
  <h1>Projets</h1>
  <p>Une sélection de projets réalisés en Business Intelligence, Data Analytics et Data Science.</p>

  <div class="project-card">
    <h3>01. Customer Churn Prediction</h3>
    <div class="project-type">Machine Learning · Telco</div>
    <p>Prédiction du risque de churn client avec Random Forest, analyse SHAP, segmentation des risques et application Streamlit.</p>
    <p><strong>Résultats :</strong> Recall 77,81 % · F1-score 63,75 % · ROC-AUC 0,85</p>
    <a class="project-link" href="./Machine-Learning/Classification/Customer-Churn-Prediction/">Voir le projet →</a>
  </div>

  <div class="project-card">
    <h3>02. Retail Analytics</h3>
    <div class="project-type">Power BI · Data Quality · DAX</div>
    <p>Analyse retail basée sur un modèle en étoile, avec audit des indicateurs, diagnostic de bugs DAX et validation des résultats.</p>
    <a class="project-link" href="./PowerBI/analyse-retail-star-schema/">Voir le projet →</a>
  </div>

  <div class="project-card">
    <h3>03. Olist E-commerce Analytics</h3>
    <div class="project-type">Power BI · E-commerce · Data Modeling</div>
    <p>Analyse d'une marketplace e-commerce brésilienne avec modélisation en constellation, contrôle des différents grains de données et analyse de la performance logistique.</p>
    <a class="project-link" href="./PowerBI/analyse-performance-olist/">Voir le projet →</a>
  </div>

  <div class="project-card">
    <h3>04. PitchSide Pro Revenue</h3>
    <div class="project-type">Power BI · Revenue Analytics · Business Intelligence</div>
    <p>Analyse de la croissance des revenus d'une plateforme e-commerce spécialisée dans les articles de football, avec décomposition du revenu entre trafic, conversion et panier moyen.</p>
    <a class="project-link" href="./PowerBI/analyse-pitchside-pro-revenue/">Voir le projet →</a>
  </div>

  <div class="project-card">
    <h3>05. Performance Football Européen</h3>
    <div class="project-type">Power BI · Sport Analytics · Scouting</div>
    <p>Analyse de la performance des joueurs et des équipes du football européen, avec des volets consacrés au scouting, aux statistiques, à la valorisation et aux effectifs.</p>
    <a class="project-link" href="./PowerBI/analyse-performance-football-europe/">Voir le projet →</a>
  </div>

  <h2>Tous mes projets</h2>
  <p><a href="./PowerBI/">Voir mes projets Power BI →</a></p>
  <p><a href="./Machine-Learning/">Voir mes projets Machine Learning →</a></p>
</section>

<section id="recherche" class="portfolio-section">
  <h1>Recherche et travaux académiques</h1>
  <h2>Diagnostic de la défécation à l'air libre dans le district de Yamoussoukro</h2>
  <p><strong>Recherche appliquée · Eau, Assainissement et Environnement · Analyse de données</strong></p>
  <p>Travail de recherche consacré au diagnostic de la défécation à l'air libre dans le district de Yamoussoukro et à l'identification des principaux facteurs associés à cette pratique.</p>

  <p><strong>Méthodologie :</strong></p>
  <ul>
    <li>Enquête auprès de 373 ménages</li>
    <li>Collecte de données sur le terrain</li>
    <li>Entretiens semi-structurés</li>
    <li>Observations directes</li>
    <li>Analyse de données socio-économiques et sanitaires</li>
    <li>Traitement et interprétation des résultats</li>
  </ul>

  <p><strong>Principaux axes d'analyse :</strong></p>
  <ul>
    <li>Accès aux infrastructures d'assainissement</li>
    <li>Pratiques de défécation à l'air libre</li>
    <li>Facteurs économiques, sociaux et culturels</li>
    <li>Niveau d'éducation et pratiques sanitaires</li>
    <li>Identification des leviers d'intervention</li>
    <li>Proposition de stratégies adaptées au contexte local</li>
  </ul>

  <p><strong>Publication :</strong> World Journal of Advanced Research and Reviews, 2024, 24(1), 1119-1125</p>
  <p><strong>Auteurs :</strong> Kinanpara KONE, Yao Francis KOUAME, Tibo Fabrice BOMISSO, Jean Renaud ALLOUKO et Kotchi Yves BONY</p>
  <p><a href="https://wjarr.com/content/diagnosis-open-defecation-yamoussoukro-district-central-cote-divoire" target="_blank" rel="noopener noreferrer">Lire la publication →</a></p>
</section>

<section id="experience" class="portfolio-section">
  <h1>Expérience</h1>
  <h2>Groupe Inova, Abidjan</h2>
  <p><strong>Stagiaire Data Analyst · Avril 2025 à Juillet 2026</strong></p>
  <ul>
    <li>Nettoyage, contrôle et préparation de données collectées par web scraping.</li>
    <li>Participation à la structuration et à l'alimentation de la base de données de l'application web.</li>
    <li>Contrôle de la qualité et de la cohérence des données avant intégration.</li>
    <li>Participation au développement d'une plateforme de visualisation.</li>
  </ul>
</section>

<section id="formation" class="portfolio-section">
  <h1>Formation</h1>

  <h2>Data Science et IA, Bootcamp</h2>
  <div class="meta-line"><strong>Fatala Digital House, en cours</strong></div>
  <p>Formation pratique en Data Science, Machine Learning et Intelligence Artificielle, avec un parcours axé sur Python, analyse de données, Machine Learning et réalisation de projets.</p>
  <p><a href="https://academy.fatala.fr/" target="_blank" rel="noopener noreferrer">Fatala Digital House →</a></p>

  <h2>Data Analyst</h2>
  <div class="meta-line"><strong>GOMYCODE, Novembre 2024 à Mars 2025</strong></div>
  <p>Formation orientée Data Analytics, Python, analyse de données et outils décisionnels.</p>
  <p><a href="https://gomycode.com/ic/fr/" target="_blank" rel="noopener noreferrer">GOMYCODE →</a></p>

  <h2>Master, Génie de l'Eau et de l'Environnement</h2>
  <p><strong>Université Jean Lorougnon Guédé</strong></p>
  <p><a href="https://ujlog.edu.ci/" target="_blank" rel="noopener noreferrer">Université Jean Lorougnon Guédé →</a></p>

  <h2>Licence, Génie de l'Eau et de l'Environnement</h2>
  <p><strong>Université Jean Lorougnon Guédé</strong></p>
  <p><a href="https://ujlog.edu.ci/" target="_blank" rel="noopener noreferrer">Université Jean Lorougnon Guédé →</a></p>
</section>

<section id="certifications" class="portfolio-section">
  <h1>Certifications</h1>
  <div class="cert-grid">
    <div class="cert-card">
      <strong>Data Analyst | GOMYCODE</strong>
      <span>Microsoft Power BI · Certificat de réussite</span><br>
      <a href="./certifications/BOMISSO%20TIBO%20FABRICE-Data%20Analytics%20-%20Microsoft%20Power%20BI%20Certified_%20Certificate%20of%20Completion.pdf">Voir le certificat →</a>
    </div>
    <div class="cert-card">
      <strong>Gestion de projet</strong>
      <span>Certificat de formation</span><br>
      <a href="./certifications/Certificat%20GESTION%20DE%20PROJET.pdf">Voir le certificat →</a>
    </div>
    <div class="cert-card">
      <strong>MEAL</strong>
      <span>Certificat MEAL</span><br>
      <a href="./certifications/Certificat%20MEAL.pdf">Voir le certificat →</a>
    </div>
    <div class="cert-card">
      <strong>WASH dans les situations d'urgence</strong>
      <span>Certificat de formation</span><br>
      <a href="./certifications/Certificat%20WASH%20dans%20les%20situations%20d'urgence.pdf">Voir le certificat →</a>
    </div>
    <div class="cert-card">
      <strong>HSE</strong>
      <span>Certificat HSE</span><br>
      <a href="./certifications/Certificat%20HSE.pdf">Voir le certificat →</a>
    </div>
    <div class="cert-card">
      <strong>Rédaction d'article scientifique</strong>
      <span>World Journal of Advanced Research and Reviews · 2024</span><br>
      <a href="./certifications/Certifact%20redaction%20d'article%20scientifique.pdf">Voir le certificat →</a><br>
      <a href="https://wjarr.com/content/diagnosis-open-defecation-yamoussoukro-district-central-cote-divoire" target="_blank" rel="noopener noreferrer">Lire la publication →</a>
    </div>
  </div>
</section>

<section id="contact" class="portfolio-section">
  <h1>Contact</h1>
  <p class="contact-line">📞 <a href="tel:+2250545778538">(+225) 05 45 77 85 38</a> · <a href="tel:+2250778314526">07 78 31 45 26</a></p>
  <p class="contact-line">📧 <a href="mailto:fabricebtibo@mail.com">fabricebtibo@mail.com</a></p>
  <p class="contact-line">📧 <a href="mailto:fabricebtibo@yahoo.com">fabricebtibo@yahoo.com</a></p>
  <p class="contact-line"><a href="https://www.linkedin.com/in/fabrice-bomisso/" target="_blank" rel="noopener noreferrer">LinkedIn</a> · <a href="https://github.com/fbomisso/fabrice.bomisso/" target="_blank" rel="noopener noreferrer">GitHub</a></p>
  <a class="cv-button" href="./documents/CV_Fabrice_Bomisso.pdf">Télécharger mon CV</a>
</section>

<div class="portfolio-footer">
  Fabrice BOMISSO · Data Analyst | Business Intelligence | Data Science
</div>

</div>

<script>
(function () {
  const sections = Array.from(document.querySelectorAll('.portfolio-section'));
  const links = Array.from(document.querySelectorAll('[data-section]'));
  const toggle = document.getElementById('theme-toggle');

  function showSection(id, updateUrl) {
    const target = document.getElementById(id) || document.getElementById('accueil');
    sections.forEach(section => section.classList.toggle('active', section === target));
    if (updateUrl) history.replaceState(null, '', '#' + target.id);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  links.forEach(link => {
    link.addEventListener('click', function (event) {
      const id = this.getAttribute('data-section');
      if (!id) return;
      event.preventDefault();
      showSection(id, true);
    });
  });

  const initial = window.location.hash ? window.location.hash.substring(1) : 'accueil';
  showSection(document.getElementById(initial) ? initial : 'accueil', false);

  const savedTheme = localStorage.getItem('fabrice-theme');
  if (savedTheme === 'dark') {
    document.body.classList.add('portfolio-dark');
    toggle.textContent = '☀';
  }

  toggle.addEventListener('click', function () {
    const dark = document.body.classList.toggle('portfolio-dark');
    localStorage.setItem('fabrice-theme', dark ? 'dark' : 'light');
    toggle.textContent = dark ? '☀' : '☾';
  });
})();
</script>
