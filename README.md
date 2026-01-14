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

### 1. Repository klonen

```properties 
git clone https://git.mylab.th-luebeck.de/max.jacobsen-mann/pumping-lemma-visualization
cd pumping-lemma-visualization
```
Abhängigkeiten installieren:
```properties 
  npm install
``` 
Entwicklungsserver starten:
```properties 
   npm run dev
```
Anwendung im Browser öffnen:
```properties 
   http://localhost:5173
```







