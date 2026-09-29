#!/usr/bin/env python3
"""Genera index.html (privacidad) y support.html (soporte) de Crimenoku en seis idiomas."""
from pathlib import Path

CORREO = "mathvirtuallearn@gmail.com"
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
AQUI = Path(__file__).parent

IDIOMAS = [("es", "Español"), ("en", "English"), ("de", "Deutsch"), ("fr", "Français"),
           ("it", "Italiano"), ("pt-BR", "Português")]

PRIVACIDAD = {
"es": ("Política de privacidad", "Crimenoku · Actualizada el 29 de septiembre de 2026",
"""<p class="resumen">Crimenoku no te pide tu nombre, ni tu correo, ni te obliga a crear ninguna cuenta.
No lleva publicidad, ni analítica, ni ningún componente de terceros que recoja datos.</p>
<h2>Lo que se queda en tu iPhone</h2>
<p>Tu progreso —casos resueltos, racha del caso del día e idioma elegido— se guarda únicamente en tu
dispositivo. No se envía a ningún servidor. Si borras la app, desaparece.</p>
<h2>Club de Detectives</h2>
<p>La suscripción es opcional y la gestiona Apple íntegramente: el cobro, la renovación y la
cancelación. No recibo tus datos de pago en ningún momento. Puedes gestionarla o cancelarla en
<em>Ajustes → tu nombre → Suscripciones</em>. Se aplican las
<a href="{eula}">condiciones de uso estándar de Apple (EULA)</a>.</p>
<h2>Lo que no hay</h2>
<ul>
<li>No hay publicidad.</li>
<li>No hay rastreo ni identificadores publicitarios.</li>
<li>No hay herramientas de analítica ni de medición de uso.</li>
<li>La app no necesita conexión a internet para jugar.</li>
<li>No se venden ni se ceden datos a nadie.</li>
</ul>
<h2>Menores</h2>
<p>La app no recoge datos personales de ninguna persona, y eso incluye a los menores.</p>
<h2>Contacto</h2>
<p>Escribe a <a href="mailto:{correo}">{correo}</a>.</p>"""),
"en": ("Privacy Policy", "Crimenoku · Updated September 29, 2026",
"""<p class="resumen">Crimenoku doesn't ask for your name or email, and you never need to create an account.
There are no ads, no analytics and no third-party components that collect data.</p>
<h2>What stays on your iPhone</h2>
<p>Your progress —solved cases, your daily case streak and your chosen language— is stored only on
your device. It is never sent to any server. If you delete the app, it's gone.</p>
<h2>Detective Club</h2>
<p>The subscription is optional and handled entirely by Apple: payment, renewal and cancellation. I
never receive your payment details. You can manage or cancel it in
<em>Settings → your name → Subscriptions</em>. Apple's
<a href="{eula}">standard Terms of Use (EULA)</a> apply.</p>
<h2>What there isn't</h2>
<ul>
<li>No advertising.</li>
<li>No tracking and no advertising identifiers.</li>
<li>No analytics or usage measurement tools.</li>
<li>No internet connection is needed to play.</li>
<li>No data is sold or shared with anyone.</li>
</ul>
<h2>Children</h2>
<p>The app collects no personal data from anyone, and that includes children.</p>
<h2>Contact</h2>
<p>Write to <a href="mailto:{correo}">{correo}</a>.</p>"""),
"de": ("Datenschutzerklärung", "Crimenoku · Stand: 29. September 2026",
"""<p class="resumen">Crimenoku fragt weder nach deinem Namen noch nach deiner E-Mail-Adresse, und du musst kein
Konto anlegen. Es gibt keine Werbung, keine Analyse-Tools und keine Komponenten von Drittanbietern,
die Daten sammeln.</p>
<h2>Was auf deinem iPhone bleibt</h2>
<p>Dein Fortschritt – gelöste Fälle, deine Serie beim Fall des Tages und die gewählte Sprache – wird
ausschließlich auf deinem Gerät gespeichert und an keinen Server gesendet. Wenn du die App löschst,
ist er weg.</p>
<h2>Detektivclub</h2>
<p>Das Abo ist freiwillig und wird vollständig von Apple abgewickelt: Zahlung, Verlängerung und
Kündigung. Ich erhalte zu keinem Zeitpunkt deine Zahlungsdaten. Du kannst es unter
<em>Einstellungen → dein Name → Abonnements</em> verwalten oder kündigen. Es gelten die
<a href="{eula}">Standard-Nutzungsbedingungen von Apple (EULA)</a>.</p>
<h2>Was es nicht gibt</h2>
<ul>
<li>Keine Werbung.</li>
<li>Kein Tracking und keine Werbe-IDs.</li>
<li>Keine Analyse- oder Messwerkzeuge.</li>
<li>Zum Spielen ist keine Internetverbindung nötig.</li>
<li>Es werden keine Daten verkauft oder weitergegeben.</li>
</ul>
<h2>Kinder</h2>
<p>Die App erhebt von niemandem personenbezogene Daten, auch nicht von Kindern.</p>
<h2>Kontakt</h2>
<p>Schreib an <a href="mailto:{correo}">{correo}</a>.</p>"""),
"fr": ("Politique de confidentialité", "Crimenoku · Mise à jour le 29 septembre 2026",
"""<p class="resumen">Crimenoku ne vous demande ni votre nom, ni votre e-mail, et vous n'avez aucun compte à
créer. Pas de publicité, pas d'outils d'analyse, aucun composant tiers qui collecte des données.</p>
<h2>Ce qui reste sur votre iPhone</h2>
<p>Votre progression — affaires résolues, série de l'affaire du jour et langue choisie — est
enregistrée uniquement sur votre appareil. Elle n'est envoyée à aucun serveur. Si vous supprimez
l'app, elle disparaît.</p>
<h2>Club des Détectives</h2>
<p>L'abonnement est facultatif et entièrement géré par Apple : paiement, renouvellement et
résiliation. Je ne reçois jamais vos données de paiement. Vous pouvez le gérer ou le résilier dans
<em>Réglages → votre nom → Abonnements</em>. Les
<a href="{eula}">conditions d'utilisation standard d'Apple (EULA)</a> s'appliquent.</p>
<h2>Ce qu'il n'y a pas</h2>
<ul>
<li>Aucune publicité.</li>
<li>Aucun pistage ni identifiant publicitaire.</li>
<li>Aucun outil d'analyse ou de mesure d'audience.</li>
<li>Aucune connexion internet n'est nécessaire pour jouer.</li>
<li>Aucune donnée n'est vendue ni cédée.</li>
</ul>
<h2>Enfants</h2>
<p>L'app ne collecte aucune donnée personnelle, y compris celles des enfants.</p>
<h2>Contact</h2>
<p>Écrivez à <a href="mailto:{correo}">{correo}</a>.</p>"""),
"it": ("Informativa sulla privacy", "Crimenoku · Aggiornata il 29 settembre 2026",
"""<p class="resumen">Crimenoku non ti chiede il nome né l'e-mail e non devi creare alcun account. Niente
pubblicità, niente strumenti di analisi, nessun componente di terze parti che raccolga dati.</p>
<h2>Cosa resta sul tuo iPhone</h2>
<p>I tuoi progressi — casi risolti, serie del caso del giorno e lingua scelta — sono salvati solo sul
tuo dispositivo. Non vengono inviati a nessun server. Se elimini l'app, spariscono.</p>
<h2>Club dei Detective</h2>
<p>L'abbonamento è facoltativo ed è gestito interamente da Apple: pagamento, rinnovo e disdetta. Non
ricevo mai i tuoi dati di pagamento. Puoi gestirlo o disdirlo in
<em>Impostazioni → il tuo nome → Abbonamenti</em>. Si applicano le
<a href="{eula}">condizioni d'uso standard di Apple (EULA)</a>.</p>
<h2>Cosa non c'è</h2>
<ul>
<li>Nessuna pubblicità.</li>
<li>Nessun tracciamento né identificatori pubblicitari.</li>
<li>Nessuno strumento di analisi o di misurazione dell'uso.</li>
<li>Per giocare non serve la connessione a internet.</li>
<li>Nessun dato viene venduto o ceduto.</li>
</ul>
<h2>Minori</h2>
<p>L'app non raccoglie dati personali di nessuno, minori compresi.</p>
<h2>Contatti</h2>
<p>Scrivi a <a href="mailto:{correo}">{correo}</a>.</p>"""),
"pt-BR": ("Política de privacidade", "Crimenoku · Atualizada em 29 de setembro de 2026",
"""<p class="resumen">O Crimenoku não pede seu nome nem seu e-mail, e você não precisa criar nenhuma conta. Não
tem publicidade, nem analytics, nem nenhum componente de terceiros que colete dados.</p>
<h2>O que fica no seu iPhone</h2>
<p>Seu progresso — casos resolvidos, sequência do caso do dia e idioma escolhido — fica guardado
apenas no seu aparelho. Não é enviado para nenhum servidor. Se apagar o app, desaparece.</p>
<h2>Clube dos Detetives</h2>
<p>A assinatura é opcional e gerenciada inteiramente pela Apple: cobrança, renovação e cancelamento.
Em nenhum momento eu recebo seus dados de pagamento. Você pode gerenciá-la ou cancelá-la em
<em>Ajustes → seu nome → Assinaturas</em>. Valem os
<a href="{eula}">termos de uso padrão da Apple (EULA)</a>.</p>
<h2>O que não existe</h2>
<ul>
<li>Não há publicidade.</li>
<li>Não há rastreamento nem identificadores de publicidade.</li>
<li>Não há ferramentas de analytics nem de medição de uso.</li>
<li>Não é preciso internet para jogar.</li>
<li>Não se vendem nem se cedem dados a ninguém.</li>
</ul>
<h2>Menores de idade</h2>
<p>O app não coleta dados pessoais de ninguém, e isso inclui menores de idade.</p>
<h2>Contato</h2>
<p>Escreva para <a href="mailto:{correo}">{correo}</a>.</p>"""),
}

SOPORTE = {
"es": ("Soporte", """<p class="resumen">¿Algún problema, un caso que no te cuadra o una idea? Escríbeme a
<a href="mailto:{correo}">{correo}</a> y dime el modelo de tu iPhone y la versión de iOS. Contesto en
cuanto puedo.</p>
<h2>Preguntas frecuentes</h2>
<h3>¿Qué es gratis?</h3>
<p>Los dos primeros capítulos (16 casos) y los tres casos del día de los lunes. El Club de Detectives
desbloquea los casos de cada día, el archivo de días anteriores y los siete capítulos.</p>
<h3>¿Cómo cancelo la suscripción?</h3>
<p>En el iPhone: <em>Ajustes → tu nombre → Suscripciones → Crimenoku</em>. Si cancelas durante la
prueba gratuita de 7 días, no se cobra nada.</p>
<h3>He cambiado de iPhone y no tengo el Club</h3>
<p>Entra en la pantalla del Club y pulsa <em>Restaurar compras</em>, con la misma cuenta de Apple.</p>
<h3>He perdido mi progreso</h3>
<p>El progreso se guarda solo en el dispositivo, así que no viaja al cambiar de teléfono ni se
recupera tras borrar la app. La suscripción sí se recupera con <em>Restaurar compras</em>.</p>
<h3>Creo que un caso no tiene solución</h3>
<p>Todos los casos tienen una única solución que se deduce sin adivinar. Relee las reglas (botón
<em>?</em>): «junto a» es solo la casilla de arriba, abajo, izquierda o derecha dentro de la misma
habitación, y el norte está arriba. El botón <em>Pista</em> te coloca a un sospechoso. Si aun así no
cuadra, escríbeme y dime qué caso es.</p>
<h3>¿En qué idiomas está?</h3>
<p>Español, inglés, alemán, francés, italiano y portugués. Sigue el idioma del teléfono y se puede
cambiar en el menú.</p>"""),
"en": ("Support", """<p class="resumen">A problem, a case that doesn't add up, or an idea? Write to
<a href="mailto:{correo}">{correo}</a> and tell me your iPhone model and iOS version. I'll reply as
soon as I can.</p>
<h2>FAQ</h2>
<h3>What's free?</h3>
<p>The first two chapters (16 cases) and the three Monday daily cases. The Detective Club unlocks every
daily case, the archive of past days and all seven chapters.</p>
<h3>How do I cancel the subscription?</h3>
<p>On your iPhone: <em>Settings → your name → Subscriptions → Crimenoku</em>. If you cancel during
the 7-day free trial, you won't be charged.</p>
<h3>I switched iPhones and lost the Club</h3>
<p>Open the Club screen and tap <em>Restore purchases</em>, using the same Apple Account.</p>
<h3>I lost my progress</h3>
<p>Progress is stored only on the device, so it doesn't move to a new phone and can't be recovered
after deleting the app. Your subscription can be recovered with <em>Restore purchases</em>.</p>
<h3>I think a case has no solution</h3>
<p>Every case has exactly one solution that can be deduced without guessing. Check the rules (the
<em>?</em> button): "next to" means only the square above, below, left or right within the same room,
and north is up. The <em>Hint</em> button places one suspect for you. If it still doesn't add up,
write to me and tell me which case it is.</p>
<h3>Which languages?</h3>
<p>Spanish, English, German, French, Italian and Portuguese. It follows your phone's language and
you can change it in the menu.</p>"""),
"de": ("Support", """<p class="resumen">Ein Problem, ein Fall, der nicht aufgeht, oder eine Idee? Schreib an
<a href="mailto:{correo}">{correo}</a> und nenne mir dein iPhone-Modell und die iOS-Version. Ich
antworte, so schnell ich kann.</p>
<h2>Häufige Fragen</h2>
<h3>Was ist kostenlos?</h3>
<p>Die ersten zwei Kapitel (16 Fälle) und die drei Fälle des Tages am Montag. Der Detektivclub schaltet
alle Fälle des Tages, das Archiv vergangener Tage und alle sieben Kapitel frei.</p>
<h3>Wie kündige ich das Abo?</h3>
<p>Auf dem iPhone: <em>Einstellungen → dein Name → Abonnements → Crimenoku</em>. Kündigst du während
der 7-tägigen Gratisphase, wird nichts berechnet.</p>
<h3>Neues iPhone, aber kein Club</h3>
<p>Öffne die Club-Seite und tippe auf <em>Käufe wiederherstellen</em> – mit demselben Apple Account.</p>
<h3>Mein Fortschritt ist weg</h3>
<p>Der Fortschritt wird nur auf dem Gerät gespeichert: Er zieht nicht auf ein neues Telefon mit und
lässt sich nach dem Löschen der App nicht wiederherstellen. Das Abo schon, mit
<em>Käufe wiederherstellen</em>.</p>
<h3>Ein Fall scheint keine Lösung zu haben</h3>
<p>Jeder Fall hat genau eine Lösung, die sich ohne Raten ableiten lässt. Lies die Regeln (Taste
<em>?</em>): „neben“ heißt nur das Feld darüber, darunter, links oder rechts im selben Raum, und
Norden ist oben. Die Taste <em>Hinweis</em> setzt einen Verdächtigen für dich. Geht es trotzdem nicht
auf, schreib mir, welcher Fall es ist.</p>
<h3>Welche Sprachen?</h3>
<p>Spanisch, Englisch, Deutsch, Französisch, Italienisch und Portugiesisch. Die App folgt der Sprache
des Telefons; im Menü kannst du sie ändern.</p>"""),
"fr": ("Assistance", """<p class="resumen">Un problème, une affaire qui ne tient pas debout ou une idée ? Écrivez à
<a href="mailto:{correo}">{correo}</a> en précisant le modèle de votre iPhone et la version d'iOS. Je
réponds dès que possible.</p>
<h2>Questions fréquentes</h2>
<h3>Qu'est-ce qui est gratuit ?</h3>
<p>Les deux premiers chapitres (16 affaires) et les trois affaires du jour du lundi. Le Club des Détectives
débloque les affaires de chaque jour, les archives des jours passés et les sept chapitres.</p>
<h3>Comment résilier l'abonnement ?</h3>
<p>Sur l'iPhone : <em>Réglages → votre nom → Abonnements → Crimenoku</em>. Si vous résiliez pendant
l'essai gratuit de 7 jours, rien n'est facturé.</p>
<h3>J'ai changé d'iPhone et je n'ai plus le Club</h3>
<p>Ouvrez l'écran du Club et touchez <em>Restaurer les achats</em>, avec le même compte Apple.</p>
<h3>J'ai perdu ma progression</h3>
<p>La progression est enregistrée uniquement sur l'appareil : elle ne suit pas sur un nouveau
téléphone et ne peut pas être récupérée après suppression de l'app. L'abonnement, lui, se récupère
avec <em>Restaurer les achats</em>.</p>
<h3>Une affaire semble sans solution</h3>
<p>Chaque affaire a une seule solution, qui se déduit sans deviner. Relisez les règles (bouton
<em>?</em>) : « à côté de » désigne seulement la case au-dessus, en dessous, à gauche ou à droite dans
la même pièce, et le nord est en haut. Le bouton <em>Indice</em> place un suspect pour vous. Si ça ne
colle toujours pas, écrivez-moi en indiquant l'affaire.</p>
<h3>Quelles langues ?</h3>
<p>Espagnol, anglais, allemand, français, italien et portugais. L'app suit la langue du téléphone et
se change dans le menu.</p>"""),
"it": ("Assistenza", """<p class="resumen">Un problema, un caso che non torna o un'idea? Scrivi a
<a href="mailto:{correo}">{correo}</a> indicando il modello del tuo iPhone e la versione di iOS.
Rispondo appena posso.</p>
<h2>Domande frequenti</h2>
<h3>Cosa è gratis?</h3>
<p>I primi due capitoli (16 casi) e i tre casi del giorno del lunedì. Il Club dei Detective sblocca i
casi di ogni giorno, l'archivio dei giorni passati e tutti e sette i capitoli.</p>
<h3>Come disdico l'abbonamento?</h3>
<p>Sull'iPhone: <em>Impostazioni → il tuo nome → Abbonamenti → Crimenoku</em>. Se disdici durante la
prova gratuita di 7 giorni, non paghi nulla.</p>
<h3>Ho cambiato iPhone e non ho più il Club</h3>
<p>Apri la schermata del Club e tocca <em>Ripristina acquisti</em>, con lo stesso Account Apple.</p>
<h3>Ho perso i progressi</h3>
<p>I progressi sono salvati solo sul dispositivo: non passano a un nuovo telefono e non si recuperano
dopo aver eliminato l'app. L'abbonamento invece si recupera con <em>Ripristina acquisti</em>.</p>
<h3>Un caso sembra senza soluzione</h3>
<p>Ogni caso ha un'unica soluzione che si deduce senza tirare a indovinare. Rileggi le regole
(pulsante <em>?</em>): «accanto a» è solo la casella sopra, sotto, a sinistra o a destra nella stessa
stanza, e il nord è in alto. Il pulsante <em>Indizio</em> sistema un sospettato al posto tuo. Se
ancora non torna, scrivimi dicendomi quale caso è.</p>
<h3>In che lingue è?</h3>
<p>Spagnolo, inglese, tedesco, francese, italiano e portoghese. Segue la lingua del telefono e si
può cambiare dal menu.</p>"""),
"pt-BR": ("Suporte", """<p class="resumen">Algum problema, um caso que não fecha ou uma ideia? Escreva para
<a href="mailto:{correo}">{correo}</a> e diga o modelo do seu iPhone e a versão do iOS. Respondo
assim que der.</p>
<h2>Perguntas frequentes</h2>
<h3>O que é grátis?</h3>
<p>Os dois primeiros capítulos (16 casos) e os três casos do dia das segundas-feiras. O Clube dos
Detetives libera os casos de todos os dias, o arquivo dos dias anteriores e os sete capítulos.</p>
<h3>Como cancelo a assinatura?</h3>
<p>No iPhone: <em>Ajustes → seu nome → Assinaturas → Crimenoku</em>. Se cancelar durante o teste
grátis de 7 dias, nada é cobrado.</p>
<h3>Troquei de iPhone e fiquei sem o Clube</h3>
<p>Abra a tela do Clube e toque em <em>Restaurar compras</em>, com a mesma Conta Apple.</p>
<h3>Perdi meu progresso</h3>
<p>O progresso fica guardado só no aparelho: não vai para um celular novo nem volta depois de apagar
o app. A assinatura, sim, volta com <em>Restaurar compras</em>.</p>
<h3>Acho que um caso não tem solução</h3>
<p>Todo caso tem uma única solução, que se deduz sem chutar. Releia as regras (botão <em>?</em>):
“junto a” é só a casa de cima, de baixo, da esquerda ou da direita dentro do mesmo aposento, e o
norte fica em cima. O botão <em>Pista</em> posiciona um suspeito para você. Se ainda assim não
fechar, me escreva dizendo qual é o caso.</p>
<h3>Em quais idiomas está?</h3>
<p>Espanhol, inglês, alemão, francês, italiano e português. Segue o idioma do celular e pode ser
trocado no menu.</p>"""),
}

TITULOS = {"index": "Privacidad · Privacy · Crimenoku", "support": "Soporte · Support · Crimenoku"}


def pagina(nombre, secciones, fecha_por_idioma, pie):
    nav = " · ".join(f'<a href="#{i}">{n}</a>' for i, n in IDIOMAS)
    partes = []
    for i, _ in IDIOMAS:
        titulo, cuerpo = secciones[i][0], secciones[i][-1]
        fecha = secciones[i][1] if fecha_por_idioma else "Crimenoku"
        partes.append(f'<section id="{i}" lang="{i}">\n<h1>{titulo}</h1>\n<p class="fecha">{fecha}</p>\n'
                      + cuerpo.format(correo=CORREO, eula=EULA) + "\n</section>")
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TITULOS[nombre]}</title>
<link rel="stylesheet" href="estilo.css">
</head>
<body>

<nav class="idiomas">{nav}</nav>

{(chr(10) + '<hr>' + chr(10)).join(partes)}

<footer>{pie}</footer>

</body>
</html>
"""
    (AQUI / f"{nombre}.html").write_text(html, encoding="utf-8")


pagina("index", PRIVACIDAD, True, '<a href="support.html">Soporte · Support</a>')
pagina("support", SOPORTE, False, '<a href="index.html">Privacidad · Privacy</a>')
print("ok")
