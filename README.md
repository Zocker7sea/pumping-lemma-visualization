# Pumping-Lemma Visualization

## Projektbeschreibung

Diese Anwendung visualisiert das Pumping-Lemma für reguläre Sprachen interaktiv.  
Ziel ist es, die abstrakte Logik des Lemmas durch eine explorative und spielerische Darstellung verständlicher zu machen.

Der Nutzer interagiert mit einer formalen Sprache und untersucht, ob gepumpte Wörter weiterhin zur Sprache gehören.  
Dabei orientiert sich die Anwendung an der klassischen Struktur des Pumping-Lemmas mit einer Zerlegung eines Wortes in die Bestandteile \(u\), \(v\) und \(w\).

Die Anwendung wurde im Rahmen einer Bachelorarbeit mit dem Titel  
**„Einfach pumpen? – Das Pumping-Lemma anschaulich erklärt“** entwickelt.

---

## Technologien

- Vue.js 3
- Vite
- Vue Router
- Tailwind CSS

---

## Voraussetzungen

Damit die Anwendung lokal gestartet werden kann, müssen folgende Werkzeuge installiert sein:

- **Node.js** (empfohlen: Version ≥ 18)
- **npm** (wird automatisch mit Node.js installiert)

---

## Lokales Starten der Anwendung

### Repository klonen

Das Projekt kann aus einem der folgenden Repositories geklont werden:

**GitLab (TH Lübeck, primäres Repository):**
```bash
git clone https://git.mylab.th-luebeck.de/max.jacobsen-mann/pumping-lemma-visualization
```
**GitHub (öffentliches Mirror-Repository):**
```bash
git clone https://github.com/Zocker7sea/pumping-lemma-visualization.git
```
Anschließend in das Projektverzeichnis wechseln:
```bash
cd pumping-lemma-visualization
```
Abhängigkeiten installieren
```bash
npm install
```
Entwicklungsserver starten
```bash
npm run dev
```
Die Anwendung ist anschließend im Browser unter folgender Adresse erreichbar:
```bash
http://localhost:5173
```

## Deployment

Das primäre Repository des Projekts wird auf dem GitLab der TH Lübeck verwaltet.  
Für das öffentliche Deployment wird das Projekt zusätzlich auf GitHub gespiegelt, da die Hosting-Plattform **Vercel** ausschließlich öffentliche Repositories unterstützt.

Das Deployment erfolgt automatisiert über Vercel und stellt die Anwendung als statische Webanwendung bereit.

### Live-Demo

Die aktuelle Version der Anwendung ist unter folgender URL erreichbar:

https://pumping-lemma-visualization.vercel.app

---

## Lizenz

Diese Anwendung wurde im Rahmen einer Bachelorarbeit entwickelt und steht unter der **MIT-Lizenz**.

Die MIT-Lizenz erlaubt die freie Nutzung, Modifikation und Weiterverbreitung des Quellcodes, auch für kommerzielle Zwecke, sofern der ursprüngliche Urheberrechtshinweis erhalten bleibt.

Weitere Informationen finden sich in der Datei [`LICENSE`](./LICENSE).