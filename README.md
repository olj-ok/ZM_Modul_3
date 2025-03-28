# ZM_Modul_3
Python Grundlagen für meine TN
## **Überblick:**
Dies ist ein interaktives Python-Quizprojekt, das mithilfe von **Tkinter** erstellt wurde. Es bietet den Teilnehmern die Möglichkeit, ihre Python-Kenntnisse spielerisch zu testen. Die Teilnehmer werden das Quiz um eigene Fragen erweitern und die Änderungen über GitHub teilen.

---

## **Projektstruktur:**

- **Master Branch:**
  - Enthält die stabile und geprüfte Version des Quiz.
  - Änderungen erfolgen nur nach Überprüfung und Testen aus dem Test Branch.

- **Test Branch:**
  - Dient zur Entwicklung und Erweiterung des Quiz.
  - Hier werden alle neuen Fragen und Funktionen getestet.

- **Feature Branches:**
  - Jeder Teilnehmer oder jedes Team erstellt einen eigenen Feature Branch (z.B. `team1-quiz-erweiterung`) vom Test Branch.
  - Änderungen werden über Pull Requests in den Test Branch integriert.

---

## **Setup:**

1. **Repository klonen:**
   ```bash
   git clone https://github.com/olj-ok/ZM_Modul_3.git
   cd ZM_Modul_3
   ```
2. **Zum Test Branch wechseln:**
   ```bash
   git checkout test
   ```
3. **Neuen Feature Branch erstellen:**
   ```bash
   git checkout -b teamname-feature
   ```
4. **Code bearbeiten und Änderungen hinzufügen:**
   ```bash
   git add .
   git commit -m "Team XYZ: Neue Quizfragen hinzugefügt"
   ```
5. **Branch pushen:**
   ```bash
   git push origin teamname-feature
   ```
6. **Pull Request erstellen:**
   - Auf GitHub eine Pull Request vom Feature Branch zum Test Branch stellen.

---

## **Aufgabe:**

1. **Erweiterung des Quiz:**
   - Ergänzen Sie das Quiz um mindestens **5 neue Fragen**.
   - Achten Sie auf die Vielfalt der Themen (z.B. Python-Grundlagen, Bibliotheken, Fehlerbehandlung).

2. **Git-Arbeitsablauf:**
   - Arbeiten Sie immer im eigenen Feature Branch.
   - Führen Sie regelmäßige Commits mit aussagekräftigen Nachrichten durch.
   - Erstellen Sie einen Pull Request zum Test Branch, wenn die Erweiterung abgeschlossen ist.

3. **Review und Merging:**
   - Der Dozent prüft die Änderungen und führt sie nach erfolgreichem Testen in den Test Branch zusammen.
   - Die stabile Version wird nach erfolgreichem Review in den Master Branch gemergt.

---

## **Nützliche Befehle:**

- **Änderungen anzeigen:**
  ```bash
  git status
  ```
- **Änderungen verfolgen:**
  ```bash
  git add .
  ```
- **Änderungen committen:**
  ```bash
  git commit -m "Beschreibung der Änderung"
  ```
- **Branch pushen:**
  ```bash
  git push origin branchname
  ```
- **Branch wechseln:**
  ```bash
  git checkout branchname
  ```

---

## **Kontakt:**
Bei Fragen wenden Sie sich bitte an Olga oder erstellen Sie ein GitHub Issue im Repository.
