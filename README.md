## Getting Started

Dieses Projekt ist ein Prototyp zur interaktiven Visualisierung des Pumping-Lemmas für reguläre Sprachen. Die Anwendung wurde mit Vue.js umgesetzt und kann lokal oder containerisiert betrieben werden.

### Voraussetzungen

Für die lokale Entwicklung werden folgende Werkzeuge benötigt:

- Node.js (empfohlen: Version ≥ 18)
- npm (wird mit Node.js installiert)
- Optional: Docker (für containerisierten Betrieb)

### Lokale Installation und Ausführung

1. Repository klonen:
   ```bash
   git clone https://git.mylab.th-luebeck.de/max.jacobsen-mann/pumping-lemma-visualization
   cd pumping-lemma-visualization


## Production Deployment (Docker)

Die Anwendung ist zustandslos (stateless) und eignet sich daher für den Betrieb in containerisierten Umgebungen wie Docker oder Kubernetes.

### Docker Deployment

Das bereitgestellte Dockerfile erstellt ein schlankes Production-Image auf Basis von Nginx. Der Build erfolgt in zwei Phasen:

1. Build der Vue.js-Anwendung
2. Auslieferung der statischen Dateien über Nginx

Das Image kann in einer Container-Orchestrierungsumgebung (z.B. Kubernetes) ohne weitere Anpassungen betrieben werden.

### Hinweise für Kubernetes / Cluster-Betrieb

- Keine persistente Speicherung notwendig
- Horizontal skalierbar
- Port 80 wird vom Container exponiert
- Konfiguration kann über Ingress oder LoadBalancer erfolgen



## Lizenz

Diese Anwendung wurde im Rahmen einer Bachelorarbeit entwickelt und steht unter der **MIT-Lizenz**.

Die MIT-Lizenz erlaubt die freie Nutzung, Modifikation und Weiterverbreitung des Quellcodes, auch für kommerzielle Zwecke, sofern der ursprüngliche Urheberrechtshinweis erhalten bleibt.

Weitere Informationen finden sich in der Datei [`LICENSE`](./LICENSE).
