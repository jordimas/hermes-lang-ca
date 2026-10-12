"""Script to apply Softcatalà translation review changes to locales/*.yaml.
"""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]

# 1. locales/ca.yaml
ca_yaml = root / "locales/ca.yaml"
content = ca_yaml.read_text(encoding="utf-8")

ca_replacements = [
    (
        "approval.summary.cancelled: La petició d’aprovació s’ha retirat o no t’ha arribat; no s’ha executat {noun}.",
        "approval.summary.cancelled: La petició d’aprovació s’ha retirat o no us ha arribat; no s’ha executat {noun}."
    ),
    (
        "approval.summary.denied: Has denegat l’execució de {noun}; no s’ha executat.",
        "approval.summary.denied: Heu denegat l’execució de {noun}; no s’ha executat."
    ),
    (
        "Torna-ho a demanar o augmenta el límit:",
        "Torneu-ho a demanar o augmenteu el límit:"
    ),
    (
        "'Filtrat per «{query}». Executa /help per veure la llista completa.'",
        "'Filtrat per «{query}». Executeu /help per veure la llista completa.'"
    ),
    (
        "'Adjunta una imatge: /image {path} o comença la instrucció amb el camí d’una imatge local'",
        "'Adjunta una imatge: /image {path} o comenceu la instrucció amb el camí d’una imatge local'"
    ),
    (
        "cli.tui.clarify_other_type_answer: Una altra opció (escriu la resposta)",
        "cli.tui.clarify_other_type_answer: Una altra opció (escriviu la resposta)"
    ),
    (
        "cli.tui.welcome: Et donem la benvinguda a Hermes Agent! Escriu el teu missatge o /help per veure les ordres.",
        "cli.tui.welcome: Us donem la benvinguda a Hermes Agent! Escriviu el vostre missatge o /help per veure les ordres."
    ),
    (
        "gateway.approval_expired: ⚠️ L’aprovació ha caducat (l’agent ja no espera). Demana a l’agent que ho torni a provar.",
        "gateway.approval_expired: ⚠️ L’aprovació ha caducat (l’agent ja no espera). Demaneu a l’agent que ho torni a provar."
    ),
    (
        "Fes servir /login o executa `hermes setup` a la màquina amfitriona.",
        "Feu servir /login o executeu `hermes setup` a la màquina amfitriona."
    ),
    (
        'gateway.background.rerun_hint: "\\nDemana’m que la torni a executar o que mostri el registre complet."',
        'gateway.background.rerun_hint: "\\nDemaneu-me que la torni a executar o que mostri el registre complet."'
    ),
    (
        "gateway.branch.no_conversation: No hi ha cap conversa de la qual crear una branca; envia primer un missatge.",
        "gateway.branch.no_conversation: No hi ha cap conversa de la qual crear una branca; envieu primer un missatge."
    ),
    (
        'gateway.compress.focus_line: \'Tema: "{topic}"\'',
        "gateway.compress.focus_line: 'Tema: «{topic}»'"
    ),
    (
        "gateway.debug.full_logs_hint: Per pujar els registres complets, executa `hermes debug share` des de la CLI.",
        "gateway.debug.full_logs_hint: Per pujar els registres complets, executeu `hermes debug share` des de la CLI."
    ),
    (
        "gateway.debug.share_hint: Comparteix aquests enllaços amb l’equip de Hermes per obtenir ajuda.",
        "gateway.debug.share_hint: Compartiu aquests enllaços amb l’equip de Hermes per obtenir ajuda."
    ),
    (
        'gateway.deny.denied_reason_plural: \'❌ S’han denegat les ordres ({count} ordres). Motiu comunicat a l’agent: "{reason}"\'',
        "gateway.deny.denied_reason_plural: '❌ S’han denegat les ordres ({count} ordres). Motiu comunicat a l’agent: «{reason}»'"
    ),
    (
        'gateway.deny.denied_reason_singular: \'❌ S’ha denegat l’ordre. Motiu comunicat a l’agent: "{reason}"\'',
        "gateway.deny.denied_reason_singular: '❌ S’ha denegat l’ordre. Motiu comunicat a l’agent: «{reason}»'"
    ),
    (
        "gateway.model.session_only_hint: _(només en aquesta sessió; afegeix `--global` per fer-ho permanent)_",
        "gateway.model.session_only_hint: _(només en aquesta sessió; afegiu `--global` per fer-ho permanent)_"
    ),
    (
        "slash.browser.description: Connecta les eines del navegador al navegador Chromium o derivat que tens obert mitjançant CDP, o canvia al mode Browser Use",
        "slash.browser.description: Connecta les eines del navegador al navegador Chromium o derivat obert mitjançant CDP, o canvia al mode Browser Use"
    ),
    (
        "slash.compress.description: Comprimeix el context de la conversa (afegeix 'here [N]' per conservar els últims N torns; --preview mostra què passaria)",
        "slash.compress.description: Comprimeix el context de la conversa (afegiu «here [N]» per conservar els últims N torns; --preview mostra què passaria)"
    ),
    (
        "slash.export.description: Exporta un perfil (configuració, habilitats i tema) a un arxiu que pots compartir",
        "slash.export.description: Exporta un perfil (configuració, habilitats i tema) a un arxiu compartible"
    ),
    (
        "slash.initiate-setup.description: Executa la configuració inicial per conèixer-te i adaptar Hermes a tu",
        "slash.initiate-setup.description: Executa la configuració inicial per conèixer-vos i adaptar Hermes a vós"
    ),
    (
        "slash.learn.description: Aprèn una habilitat reutilitzable a partir del que descriguis (directoris, URL, aquest xat o notes)",
        "slash.learn.description: Aprèn una habilitat reutilitzable a partir del que descrigueu (directoris, URL, aquest xat o notes)"
    ),
    (
        "slash.pause.description: Atura globalment la feina nova (aturada d’emergència); '/pause off' la reprèn",
        "slash.pause.description: Atura globalment la feina nova (aturada d’emergència); «/pause off» la reprèn"
    ),
    (
        "slash.resume.description: Reprèn una sessió a la qual has assignat un nom",
        "slash.resume.description: Reprèn una sessió anomenada anteriorment"
    ),
    (
        "slash.review.description: Crea un subagent independent per revisar la feina que acabes de comentar (PR, codi o documentació)",
        "slash.review.description: Crea un subagent independent per revisar la feina que s’acaba de comentar (PR, codi o documentació)"
    ),
    (
        "slash.wake.description: Activa o desactiva la detecció de la paraula d’activació 'Hey Hermes'",
        "slash.wake.description: Activa o desactiva la detecció de la paraula d’activació «Hey Hermes»"
    ),
    (
        "slash.whoami.description: Mostra el teu nivell d’accés a les ordres (administrador o usuari)",
        "slash.whoami.description: Mostra el nivell d’accés a les ordres (administrador o usuari)"
    ),
    (
        "tips.placeholder.p01: Pregunta el que vulguis o escriu / per veure les ordres…",
        "tips.placeholder.p01: Pregunteu el que vulgueu o escriviu / per veure les ordres…"
    ),
    (
        "tips.placeholder.p11: Escriu / per explorar les ordres o Ctrl+P per obrir la paleta",
        "tips.placeholder.p11: Escriviu / per explorar les ordres o Ctrl+P per obrir la paleta"
    ),
    (
        'tips.t007: /title "my project" dona un nom a la sessió; reprèn-la més endavant amb /resume o hermes -c.',
        'tips.t007: /title "my project" dona un nom a la sessió; repreneu-la més endavant amb /resume o hermes -c.'
    ),
    (
        "tips.t008: /resume reprèn una sessió amb nom des d’on la vas deixar.",
        "tips.t008: /resume reprèn una sessió amb nom des d’on la vau deixar."
    ),
    (
        "tips.t016: /model permet canviar de model durant la sessió; prova /model sonnet o /model gpt-5.",
        "tips.t016: /model permet canviar de model durant la sessió; proveu /model sonnet o /model gpt-5."
    ),
    (
        "tips.t019: /skin canvia el tema de la CLI; prova ares, mono, slate, poseidon o charizard.",
        "tips.t019: /skin canvia el tema de la CLI; proveu ares, mono, slate, poseidon o charizard."
    ),
    (
        "tips.t022: /browser connect connecta les eines del navegador al navegador Chromium o derivat que tens obert mitjançant CDP.",
        "tips.t022: /browser connect connecta les eines del navegador al navegador Chromium o derivat que teniu obert mitjançant CDP."
    ),
    (
        "tips.t035: @diff incorpora al missatge els canvis de Git que no has afegit a l’índex.",
        "tips.t035: @diff incorpora al missatge els canvis de Git que no heu afegit a l’índex."
    ),
    (
        "tips.t036: @staged incorpora els canvis de Git que has afegit a l’índex (git diff --staged).",
        "tips.t036: @staged incorpora els canvis de Git que heu afegit a l’índex (git diff --staged)."
    ),
    (
        '\'Combina diverses referències: "Revisa @file:main.py i @file:test.py per comprovar que són coherents."\'',
        "'Combina diverses referències: «Revisa @file:main.py i @file:test.py per comprovar que són coherents.»'"
    ),
    (
        "tips.t041: Alt+Enter insereix una línia nova. (El Windows Terminal intercepta Alt+Enter; utilitza Ctrl+Enter.)",
        "tips.t041: Alt+Enter insereix una línia nova. (El Windows Terminal intercepta Alt+Enter; utilitzeu Ctrl+Enter.)"
    ),
    (
        "tips.t042: Ctrl+C interromp l’agent. Prem-lo dues vegades en menys de 2 segons per forçar la sortida.",
        "tips.t042: Ctrl+C interromp l’agent. Premeu-lo dues vegades en menys de 2 segons per forçar la sortida."
    ),
    (
        "tips.t043: Ctrl+Z suspèn Hermes en segon pla; executa fg a l’intèrpret d’ordres per reprendre’l.",
        "tips.t043: Ctrl+Z suspèn Hermes en segon pla; executeu fg a l’intèrpret d’ordres per reprendre’l."
    ),
    (
        "tips.t045: Escriu un missatge nou mentre l’agent treballa per interrompre’l i redirigir-lo.",
        "tips.t045: Escriviu un missatge nou mentre l’agent treballa per interrompre’l i redirigir-lo."
    ),
    (
        "tips.t047: Si enganxes 5 línies o més, es desen automàticament en un fitxer i s’hi insereix una referència compacta.",
        "tips.t047: Si enganxeu 5 línies o més, es desen automàticament en un fitxer i s’hi insereix una referència compacta."
    ),
]

for old, new in ca_replacements:
    if old not in content:
        print(f"ERROR: not found in ca.yaml: {old!r}", file=sys.stderr)
        sys.exit(1)
    content = content.replace(old, new)

ca_yaml.write_text(content, encoding="utf-8")
print(f"Updated {ca_yaml.name} with {len(ca_replacements)} replacements.")

# 2. locales/ca.tui.yaml
ca_tui = root / "locales/ca.tui.yaml"
tui_content = ca_tui.read_text(encoding="utf-8")

tui_replacements = [
    (
        "composer.placeholders.ask: Pregunta’m el que vulguis…",
        "composer.placeholders.ask: Pregunteu-me el que vulgueu…"
    ),
    (
        "composer.placeholders.config: Prova «com funciona el carregador de configuració?»",
        "composer.placeholders.config: Proveu «com funciona el carregador de configuració?»"
    ),
    (
        "composer.placeholders.explain: Prova «explica aquest projecte»",
        "composer.placeholders.explain: Proveu «explica aquest projecte»"
    ),
    (
        "composer.placeholders.help: Prova «/help» per veure les ordres",
        "composer.placeholders.help: Proveu «/help» per veure les ordres"
    ),
    (
        "composer.placeholders.lint: Prova «corregeix els errors del linter»",
        "composer.placeholders.lint: Proveu «corregeix els errors del linter»"
    ),
    (
        "composer.placeholders.refactor: Prova «refactoritza el mòdul d’autenticació»",
        "composer.placeholders.refactor: Proveu «refactoritza el mòdul d’autenticació»"
    ),
    (
        "composer.placeholders.test: Prova «escriu una prova per a…»",
        "composer.placeholders.test: Proveu «escriu una prova per a…»"
    ),
    (
        "help.quickHelpTail: '  ·  escriu /help per obrir el tauler complet  ·  retrocés per tancar'",
        "help.quickHelpTail: '  ·  escriviu /help per obrir el tauler complet  ·  retrocés per tancar'"
    ),
    (
        "hints.discardDraft: descarta l’esborrany (recupera’l amb ↑)",
        "hints.discardDraft: descarta l’esborrany (recupereu-lo amb ↑)"
    ),
    (
        "hints.sessionSwitcher: obre el selector de sessions actives (suprimeix el missatge de la cua mentre l’edites)",
        "hints.sessionSwitcher: obre el selector de sessions actives (suprimeix el missatge de la cua mentre s’edita)"
    ),
    (
        "prompt.clarify.other: Una altra opció (escriu la resposta)",
        "prompt.clarify.other: Una altra opció (escriviu la resposta)"
    ),
    (
        "session.input.voiceStillTranscribing: 'veu: encara s’està transcrivint; torna-ho a provar d’aquí a un moment'",
        "session.input.voiceStillTranscribing: 'veu: encara s’està transcrivint; torneu-ho a provar d’aquí a un moment'"
    ),
    (
        "session.lifecycle.interruptBeforeSwitch: interromp el torn actual abans de provar de {0}",
        "session.lifecycle.interruptBeforeSwitch: interrompeu el torn actual abans de provar de {0}"
    ),
    (
        "session.main.widgetLive: el giny /{0} està actiu; escriu /{0} per obrir-lo",
        "session.main.widgetLive: el giny /{0} està actiu; escriviu /{0} per obrir-lo"
    ),
]

for old, new in tui_replacements:
    if old not in tui_content:
        print(f"ERROR: not found in ca.tui.yaml: {old!r}", file=sys.stderr)
        sys.exit(1)
    tui_content = tui_content.replace(old, new)

ca_tui.write_text(tui_content, encoding="utf-8")
print(f"Updated {ca_tui.name} with {len(tui_replacements)} replacements.")

# 3. locales/ca.desktop.yaml
ca_desktop = root / "locales/ca.desktop.yaml"
desktop_content = ca_desktop.read_text(encoding="utf-8")

desktop_replacements = [
    (
        "assistant.clarify.other: Una altra opció (escriu la resposta)",
        "assistant.clarify.other: Una altra opció (escriviu la resposta)"
    ),
    (
        "common.tryHint: Prova «{0}»",
        "common.tryHint: Proveu «{0}»"
    ),
    (
        "composer.lookupTry: Prova",
        "composer.lookupTry: Proveu"
    ),
    (
        "fileMenu.deleteTitle: Vols suprimir {0}?",
        "fileMenu.deleteTitle: Voleu suprimir {0}?"
    ),
    (
        "fileMenu.deleteBody: Es mourà a la paperera; el podràs restaurar des d’allà.",
        "fileMenu.deleteBody: Es mourà a la paperera; el podreu restaurar des d’allà."
    ),
    (
        "sidebar.row.deleteTitle: Vols suprimir la sessió?",
        "sidebar.row.deleteTitle: Voleu suprimir la sessió?"
    ),
    (
        "sidebar.row.needsInput: Cal que responguis",
        "sidebar.row.needsInput: Cal una resposta"
    ),
    (
        "sidebar.row.renameDesc: Deixa-ho buit per esborrar-ho.",
        "sidebar.row.renameDesc: Deixeu-ho buit per esborrar-ho."
    ),
    (
        "sidebar.row.waitingForAnswer: S’està esperant la teva resposta",
        "sidebar.row.waitingForAnswer: S’està esperant la vostra resposta"
    ),
    (
        "sidebar.shiftClickHint: Fes Maj+clic en un xat per fixar-lo",
        "sidebar.shiftClickHint: Feu Maj+clic en un xat per fixar-lo"
    ),
]

for old, new in desktop_replacements:
    if old not in desktop_content:
        print(f"ERROR: not found in ca.desktop.yaml: {old!r}", file=sys.stderr)
        sys.exit(1)
    desktop_content = desktop_content.replace(old, new)

ca_desktop.write_text(desktop_content, encoding="utf-8")
print(f"Updated {ca_desktop.name} with {len(desktop_replacements)} replacements.")
