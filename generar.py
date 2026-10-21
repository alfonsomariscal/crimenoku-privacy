#!/usr/bin/env python3
"""Genera index.html (privacidad) y support.html (soporte) de Crimenoku en seis idiomas."""
from pathlib import Path

CORREO = "mathvirtuallearn@gmail.com"
EULA = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/"
AQUI = Path(__file__).parent

IDIOMAS = [("es", "Español"), ("en", "English"), ("de", "Deutsch"), ("fr", "Français"),
           ("it", "Italiano"), ("pt-BR", "Português")]

PRIVACIDAD = {'es': ('Política de privacidad',
        'Crimenoku · Actualizada el 21 de octubre de 2026',
        '<h2>Tu juego y el ranking</h2><p>Puedes jugar sin participar en la clasificación. El progreso, las placas y '
        'el idioma se guardan en el dispositivo. No hay publicidad, rastreo publicitario ni Analytics.</p>\n'
        '<h2>Participación voluntaria</h2><p>Al elegir un alias se crea una identidad anónima con Firebase '
        'Authentication (Google). Cloud Firestore guarda el alias, identificador, resultados, puntos y pertenencia al '
        'grupo para validar casos y mostrar clasificaciones. El alias y la puntuación semanal son visibles para los '
        'participantes; los grupos solo son accesibles a sus miembros mediante un código de invitación. Evita nombres '
        'reales, correos u otros datos personales en alias y nombres de grupo.</p>\n'
        '<h2>Proveedores y conservación</h2><p>Firebase procesa estos datos para prestar el servicio. La base de datos '
        'de resultados está en Madrid; otros servicios de Google pueden procesar información técnica de conexión, como '
        'la dirección IP, en otras ubicaciones conforme a sus condiciones. No vendemos datos ni los usamos para '
        'publicidad. Los datos del ranking se conservan hasta que eliminas el perfil. Consulta la <a '
        'href="https://firebase.google.com/support/privacy">privacidad de Firebase</a>.</p>\n'
        '<h2>Eliminar tus datos</h2><p>En Detectives → Semanal → Eliminar perfil en línea puedes borrar tu identidad, '
        'alias, resultados y pertenencia al grupo. Se conserva el progreso local. Desinstalar la app no elimina los '
        'datos del servidor y puede hacerte perder el acceso al perfil: elimínalo antes desde la app. No existe '
        'recuperación ni sincronización entre dispositivos. Para solicitar acceso, rectificación o eliminación, '
        'escribe a {correo}; necesitaremos información suficiente para identificar tu perfil sin pedir datos de '
        'pago.</p>\n'
        '<h2>Club de Detectives</h2><p>Apple gestiona el cobro, las renovaciones y las cancelaciones. No recibimos tus '
        'datos de pago. Eliminar el perfil del ranking no cancela una suscripción: gestiónala en Ajustes → tu nombre → '
        'Suscripciones. Se aplican las <a href="{eula}">condiciones de uso de Apple</a>.</p>\n'
        '<h2>Responsable y contacto</h2><p>Alfonso Mariscal. Contacto: <a href="mailto:{correo}">{correo}</a>. No '
        'incluyas datos personales de menores en la clasificación; pueden jugar sin activar el ranking.</p>\n'),
 'en': ('Privacy Policy',
        'Crimenoku · Updated October 21, 2026',
        '<h2>Your game and leaderboard</h2><p>You can play without joining the leaderboard. Progress, badges and '
        'language are stored on your device. There are no ads, advertising tracking or Analytics.</p>\n'
        '<h2>Optional participation</h2><p>Choosing an alias creates an anonymous identity with Firebase '
        'Authentication (Google). Cloud Firestore stores your alias, identifier, results, points and group membership '
        'to validate cases and display rankings. Participants can see aliases and weekly scores. Groups are accessible '
        'only to members via an invitation code. Do not use real names, emails or personal information in aliases or '
        'group names.</p>\n'
        '<h2>Providers and retention</h2><p>Firebase processes this data to provide the service. The results database '
        'is in Madrid; other Google services may process connection information such as IP addresses elsewhere under '
        'their terms. We do not sell data or use it for advertising. Leaderboard data is retained until you delete '
        'your profile. See <a href="https://firebase.google.com/support/privacy">Firebase privacy</a>.</p>\n'
        '<h2>Delete your data</h2><p>In Detectives → Weekly → Delete online profile you can delete your identity, '
        'alias, results and group membership. Local progress remains. Uninstalling does not delete server data and may '
        'lose access to your profile: delete it in the app first. There is no account recovery or cross-device '
        'synchronization. Contact {correo} for access, correction or deletion; we need enough information to identify '
        'your profile, never payment details.</p>\n'
        '<h2>Detective Club</h2><p>Apple handles payments, renewal and cancellation. We do not receive payment '
        'details. Deleting your leaderboard profile does not cancel your subscription; manage it in Settings → your '
        'name → Subscriptions. <a href="{eula}">Apple Terms of Use</a> apply.</p>\n'
        '<h2>Controller and contact</h2><p>Alfonso Mariscal: <a href="mailto:{correo}">{correo}</a>. Do not enter '
        'children’s personal information in the leaderboard; they can play without activating it.</p>\n'),
 'de': ('Datenschutzerklärung',
        'Crimenoku · Stand: 21. Oktober 2026',
        '<h2>Spiel und Rangliste</h2><p>Du kannst ohne Rangliste spielen. Fortschritt, Marken und Sprache bleiben auf '
        'deinem Gerät. Es gibt keine Werbung, kein Werbetracking und kein Analytics.</p>\n'
        '<h2>Freiwillige Teilnahme</h2><p>Mit einem Alias wird eine anonyme Identität über Firebase Authentication '
        '(Google) erstellt. Cloud Firestore speichert Alias, Kennung, Ergebnisse, Punkte und Gruppenzugehörigkeit zur '
        'Prüfung von Fällen und Anzeige der Ranglisten. Teilnehmer sehen Alias und Wochenpunkte. Gruppen sind nur für '
        'Mitglieder mit Einladungscode zugänglich. Verwende keine echten Namen, E-Mail-Adressen oder persönlichen '
        'Angaben.</p>\n'
        '<h2>Anbieter und Speicherung</h2><p>Firebase verarbeitet diese Daten für den Dienst. Die Ergebnisdatenbank '
        'liegt in Madrid; andere Google-Dienste können technische Verbindungsdaten wie IP-Adressen gemäß ihren '
        'Bedingungen andernorts verarbeiten. Wir verkaufen keine Daten und nutzen sie nicht für Werbung. '
        'Ranglistendaten bleiben bis zur Profillöschung gespeichert. <a '
        'href="https://firebase.google.com/support/privacy">Firebase-Datenschutz</a>.</p>\n'
        '<h2>Daten löschen</h2><p>Unter Detectives → Wöchentlich → Online-Profil löschen kannst du Identität, Alias, '
        'Ergebnisse und Gruppenzugehörigkeit entfernen. Lokaler Fortschritt bleibt erhalten. Deinstallation löscht '
        'keine Serverdaten und kann den Profilzugriff verlieren lassen: lösche das Profil vorher in der App. Keine '
        'Wiederherstellung oder Gerätesynchronisierung. Für Auskunft, Berichtigung oder Löschung: {correo}. Wir '
        'benötigen Angaben zur Identifizierung des Profils, keine Zahlungsdaten.</p>\n'
        '<h2>Detektivclub</h2><p>Apple verwaltet Zahlung, Verlängerung und Kündigung. Wir erhalten keine '
        'Zahlungsdaten. Die Profillöschung kündigt das Abo nicht. Verwalte es unter Einstellungen → dein Name → '
        'Abonnements. Es gelten die <a href="{eula}">Apple-Nutzungsbedingungen</a>.</p>\n'
        '<h2>Verantwortlicher</h2><p>Alfonso Mariscal: <a href="mailto:{correo}">{correo}</a>. Keine persönlichen '
        'Daten von Kindern in der Rangliste angeben; Spielen ist ohne Rangliste möglich.</p>\n'),
 'fr': ('Politique de confidentialité',
        'Crimenoku · Mise à jour le 21 octobre 2026',
        '<h2>Jeu et classement</h2><p>Vous pouvez jouer sans participer au classement. Progression, insignes et langue '
        'restent sur votre appareil. Aucune publicité, aucun suivi publicitaire ni Analytics.</p>\n'
        '<h2>Participation facultative</h2><p>Choisir un pseudo crée une identité anonyme avec Firebase Authentication '
        '(Google). Cloud Firestore conserve pseudo, identifiant, résultats, points et groupe pour valider les enquêtes '
        'et afficher le classement. Les participants voient les pseudos et scores hebdomadaires. Les groupes sont '
        'accessibles uniquement aux membres via un code d’invitation. Évitez noms réels, e-mails et données '
        'personnelles.</p>\n'
        '<h2>Prestataires et conservation</h2><p>Firebase traite ces données pour fournir le service. La base des '
        'résultats est à Madrid ; d’autres services Google peuvent traiter des informations de connexion, comme '
        'l’adresse IP, ailleurs selon leurs conditions. Aucune vente ni utilisation publicitaire des données. '
        'Conservation jusqu’à suppression du profil. <a '
        'href="https://firebase.google.com/support/privacy">Confidentialité Firebase</a>.</p>\n'
        '<h2>Supprimer vos données</h2><p>Dans Détectives → Hebdomadaire → Supprimer le profil en ligne, effacez '
        'identité, pseudo, résultats et appartenance au groupe. La progression locale reste. Désinstaller ne supprime '
        'pas les données du serveur et peut faire perdre l’accès : supprimez d’abord le profil dans l’app. Aucune '
        'récupération ni synchronisation entre appareils. Pour accès, rectification ou suppression : {correo}. Nous '
        'demandons les informations nécessaires pour identifier le profil, jamais les données de paiement.</p>\n'
        '<h2>Club des Détectives</h2><p>Apple gère paiements, renouvellements et résiliations. Nous ne recevons pas '
        'vos données de paiement. Supprimer le profil ne résilie pas l’abonnement : gérez-le dans Réglages → votre nom '
        '→ Abonnements. <a href="{eula}">Conditions Apple</a>.</p>\n'
        '<h2>Responsable</h2><p>Alfonso Mariscal : <a href="mailto:{correo}">{correo}</a>. N’inscrivez aucune donnée '
        'personnelle d’enfant au classement ; il est possible de jouer sans l’activer.</p>\n'),
 'it': ('Informativa sulla privacy',
        'Crimenoku · Aggiornata il 21 ottobre 2026',
        '<h2>Gioco e classifica</h2><p>Puoi giocare senza partecipare alla classifica. Progressi, distintivi e lingua '
        'rimangono sul dispositivo. Nessuna pubblicità, tracciamento pubblicitario o Analytics.</p>\n'
        '<h2>Partecipazione facoltativa</h2><p>Scegliendo un alias crei un’identità anonima con Firebase '
        'Authentication (Google). Cloud Firestore conserva alias, identificativo, risultati, punti e gruppo per '
        'verificare i casi e mostrare le classifiche. I partecipanti vedono alias e punteggi settimanali. I gruppi '
        'sono accessibili solo ai membri tramite codice d’invito. Evita nomi reali, e-mail e dati personali.</p>\n'
        '<h2>Fornitori e conservazione</h2><p>Firebase elabora questi dati per fornire il servizio. Il database dei '
        'risultati è a Madrid; altri servizi Google possono elaborare dati tecnici di connessione come indirizzi IP '
        'altrove secondo le loro condizioni. Non vendiamo dati né li usiamo per pubblicità. I dati restano fino '
        'all’eliminazione del profilo. <a href="https://firebase.google.com/support/privacy">Privacy '
        'Firebase</a>.</p>\n'
        '<h2>Eliminare i dati</h2><p>In Detective → Settimanale → Elimina profilo online puoi cancellare identità, '
        'alias, risultati e appartenenza al gruppo. I progressi locali restano. Disinstallare non cancella i dati sul '
        'server e può far perdere l’accesso: elimina prima il profilo nell’app. Nessun recupero o sincronizzazione tra '
        'dispositivi. Per accesso, rettifica o eliminazione: {correo}. Servono informazioni per identificare il '
        'profilo, mai dati di pagamento.</p>\n'
        '<h2>Club dei Detective</h2><p>Apple gestisce pagamenti, rinnovi e cancellazioni. Non riceviamo dati di '
        'pagamento. Eliminare il profilo non annulla l’abbonamento: gestiscilo in Impostazioni → il tuo nome → '
        'Abbonamenti. Si applicano le <a href="{eula}">condizioni Apple</a>.</p>\n'
        '<h2>Titolare</h2><p>Alfonso Mariscal: <a href="mailto:{correo}">{correo}</a>. Non inserire dati personali di '
        'minori in classifica; possono giocare senza attivarla.</p>\n'),
 'pt-BR': ('Política de privacidade',
           'Crimenoku · Atualizada em 21 de outubro de 2026',
           '<h2>Jogo e classificação</h2><p>Você pode jogar sem participar da classificação. Progresso, insígnias e '
           'idioma ficam no dispositivo. Não há anúncios, rastreamento publicitário nem Analytics.</p>\n'
           '<h2>Participação opcional</h2><p>Escolher um apelido cria uma identidade anônima com Firebase '
           'Authentication (Google). Cloud Firestore armazena apelido, identificador, resultados, pontos e grupo para '
           'validar casos e mostrar classificações. Participantes veem apelidos e pontuações semanais. Grupos são '
           'acessíveis apenas aos membros por código de convite. Evite nomes reais, e-mails e dados pessoais.</p>\n'
           '<h2>Fornecedores e retenção</h2><p>Firebase processa esses dados para prestar o serviço. O banco de '
           'resultados fica em Madri; outros serviços Google podem processar dados técnicos de conexão, como IP, em '
           'outros locais conforme seus termos. Não vendemos dados nem os usamos para publicidade. Os dados ficam até '
           'a exclusão do perfil. <a href="https://firebase.google.com/support/privacy">Privacidade Firebase</a>.</p>\n'
           '<h2>Excluir dados</h2><p>Em Detetives → Semanal → Excluir perfil online, você pode apagar identidade, '
           'apelido, resultados e participação no grupo. O progresso local fica. Desinstalar não apaga dados do '
           'servidor e pode causar perda de acesso: exclua primeiro o perfil no app. Não há recuperação nem '
           'sincronização entre dispositivos. Para acesso, correção ou exclusão: {correo}. Precisamos de informações '
           'para identificar o perfil, nunca dados de pagamento.</p>\n'
           '<h2>Clube dos Detetives</h2><p>Apple gerencia pagamentos, renovações e cancelamentos. Não recebemos dados '
           'de pagamento. Excluir o perfil não cancela a assinatura: gerencie em Ajustes → seu nome → Assinaturas. '
           'Aplicam-se os <a href="{eula}">termos Apple</a>.</p>\n'
           '<h2>Responsável</h2><p>Alfonso Mariscal: <a href="mailto:{correo}">{correo}</a>. Não coloque dados '
           'pessoais de menores na classificação; eles podem jogar sem ativá-la.</p>\n')}

SOPORTE = {'es': ('Soporte',
        '<p class="resumen">¿Algún problema, un caso que no te cuadra o una idea? Escríbeme a\n'
        '<a href="mailto:{correo}">{correo}</a> y dime el modelo de tu iPhone y la versión de iOS. Contesto en\n'
        'cuanto puedo.</p>\n'
        '<h2>Preguntas frecuentes</h2>\n'
        '<h3>¿Qué es gratis?</h3>\n'
        '<p>Los dos primeros capítulos (16 casos) y los tres retos de hoy, todos los días. El Club de Detectives '
        'incluye el archivo de días anteriores y los dieciséis capítulos completos.</p>\n'
        '<h3>¿Cómo cancelo la suscripción?</h3>\n'
        '<p>En el iPhone: <em>Ajustes → tu nombre → Suscripciones → Crimenoku</em>. Consulta allí la fecha de '
        'renovación y las condiciones de cualquier prueba disponible. Cancela al menos 24 horas antes del final del '
        'periodo para evitar la renovación.</p>\n'
        '<h3>He cambiado de iPhone y no tengo el Club</h3>\n'
        '<p>Entra en la pantalla del Club y pulsa <em>Restaurar compras</em>, con la misma cuenta de Apple.</p>\n'
        '<h3>He perdido mi progreso</h3>\n'
        '<p>El progreso se guarda solo en el dispositivo, así que no viaja al cambiar de teléfono ni se\n'
        'recupera tras borrar la app. La suscripción sí se recupera con <em>Restaurar compras</em>.</p>\n'
        '<h3>Creo que un caso no tiene solución</h3>\n'
        '<p>Todos los casos tienen una única solución que se deduce sin adivinar. Relee las reglas (botón\n'
        '<em>?</em>): «junto a» es solo la casilla de arriba, abajo, izquierda o derecha dentro de la misma\n'
        'habitación, y el norte está arriba. El botón <em>Pista</em> te coloca a un sospechoso. Si aun así no\n'
        'cuadra, escríbeme y dime qué caso es.</p>\n'
        '<h3>¿En qué idiomas está?</h3>\n'
        '<p>Español, inglés, alemán, francés, italiano y portugués. Sigue el idioma del teléfono y se puede\n'
        'cambiar en el menú.</p>'),
 'en': ('Support',
        '<p class="resumen">A problem, a case that doesn\'t add up, or an idea? Write to\n'
        '<a href="mailto:{correo}">{correo}</a> and tell me your iPhone model and iOS version. I\'ll reply as\n'
        'soon as I can.</p>\n'
        '<h2>FAQ</h2>\n'
        "<h3>What's free?</h3>\n"
        '<p>The first two chapters (16 cases) and today’s three challenges, every day. The Detective Club includes the '
        'archive of previous days and all sixteen chapters.</p>\n'
        '<h3>How do I cancel the subscription?</h3>\n'
        '<p>On iPhone: <em>Settings → your name → Subscriptions → Crimenoku</em>. Check the renewal date and terms of '
        'any available trial there. Cancel at least 24 hours before the period ends to avoid renewal.</p>\n'
        '<h3>I switched iPhones and lost the Club</h3>\n'
        '<p>Open the Club screen and tap <em>Restore purchases</em>, using the same Apple Account.</p>\n'
        '<h3>I lost my progress</h3>\n'
        "<p>Progress is stored only on the device, so it doesn't move to a new phone and can't be recovered\n"
        'after deleting the app. Your subscription can be recovered with <em>Restore purchases</em>.</p>\n'
        '<h3>I think a case has no solution</h3>\n'
        '<p>Every case has exactly one solution that can be deduced without guessing. Check the rules (the\n'
        '<em>?</em> button): "next to" means only the square above, below, left or right within the same room,\n'
        "and north is up. The <em>Hint</em> button places one suspect for you. If it still doesn't add up,\n"
        'write to me and tell me which case it is.</p>\n'
        '<h3>Which languages?</h3>\n'
        "<p>Spanish, English, German, French, Italian and Portuguese. It follows your phone's language and\n"
        'you can change it in the menu.</p>'),
 'de': ('Support',
        '<p class="resumen">Ein Problem, ein Fall, der nicht aufgeht, oder eine Idee? Schreib an\n'
        '<a href="mailto:{correo}">{correo}</a> und nenne mir dein iPhone-Modell und die iOS-Version. Ich\n'
        'antworte, so schnell ich kann.</p>\n'
        '<h2>Häufige Fragen</h2>\n'
        '<h3>Was ist kostenlos?</h3>\n'
        '<p>Die ersten zwei Kapitel (16 Fälle) und die drei heutigen Herausforderungen, jeden Tag. Der Detektivclub '
        'umfasst das Archiv vergangener Tage und alle sechzehn Kapitel.</p>\n'
        '<h3>Wie kündige ich das Abo?</h3>\n'
        '<p>Auf dem iPhone: <em>Einstellungen → dein Name → Abonnements → Crimenoku</em>. Dort findest du '
        'Verlängerungsdatum und Bedingungen einer verfügbaren Testphase. Kündige mindestens 24 Stunden vor Ablauf, um '
        'eine Verlängerung zu vermeiden.</p>\n'
        '<h3>Neues iPhone, aber kein Club</h3>\n'
        '<p>Öffne die Club-Seite und tippe auf <em>Käufe wiederherstellen</em> – mit demselben Apple Account.</p>\n'
        '<h3>Mein Fortschritt ist weg</h3>\n'
        '<p>Der Fortschritt wird nur auf dem Gerät gespeichert: Er zieht nicht auf ein neues Telefon mit und\n'
        'lässt sich nach dem Löschen der App nicht wiederherstellen. Das Abo schon, mit\n'
        '<em>Käufe wiederherstellen</em>.</p>\n'
        '<h3>Ein Fall scheint keine Lösung zu haben</h3>\n'
        '<p>Jeder Fall hat genau eine Lösung, die sich ohne Raten ableiten lässt. Lies die Regeln (Taste\n'
        '<em>?</em>): „neben“ heißt nur das Feld darüber, darunter, links oder rechts im selben Raum, und\n'
        'Norden ist oben. Die Taste <em>Hinweis</em> setzt einen Verdächtigen für dich. Geht es trotzdem nicht\n'
        'auf, schreib mir, welcher Fall es ist.</p>\n'
        '<h3>Welche Sprachen?</h3>\n'
        '<p>Spanisch, Englisch, Deutsch, Französisch, Italienisch und Portugiesisch. Die App folgt der Sprache\n'
        'des Telefons; im Menü kannst du sie ändern.</p>'),
 'fr': ('Assistance',
        '<p class="resumen">Un problème, une affaire qui ne tient pas debout ou une idée ? Écrivez à\n'
        '<a href="mailto:{correo}">{correo}</a> en précisant le modèle de votre iPhone et la version d\'iOS. Je\n'
        'réponds dès que possible.</p>\n'
        '<h2>Questions fréquentes</h2>\n'
        "<h3>Qu'est-ce qui est gratuit ?</h3>\n"
        '<p>Les deux premiers chapitres (16 enquêtes) et les trois défis du jour, chaque jour. Le Club des Détectives '
        'comprend les archives des jours précédents et les seize chapitres complets.</p>\n'
        "<h3>Comment résilier l'abonnement ?</h3>\n"
        '<p>Sur iPhone : <em>Réglages → votre nom → Abonnements → Crimenoku</em>. Consultez la date de renouvellement '
        'et les conditions d’un éventuel essai. Résiliez au moins 24 heures avant la fin de la période pour éviter le '
        'renouvellement.</p>\n'
        "<h3>J'ai changé d'iPhone et je n'ai plus le Club</h3>\n"
        "<p>Ouvrez l'écran du Club et touchez <em>Restaurer les achats</em>, avec le même compte Apple.</p>\n"
        "<h3>J'ai perdu ma progression</h3>\n"
        "<p>La progression est enregistrée uniquement sur l'appareil : elle ne suit pas sur un nouveau\n"
        "téléphone et ne peut pas être récupérée après suppression de l'app. L'abonnement, lui, se récupère\n"
        'avec <em>Restaurer les achats</em>.</p>\n'
        '<h3>Une affaire semble sans solution</h3>\n'
        '<p>Chaque affaire a une seule solution, qui se déduit sans deviner. Relisez les règles (bouton\n'
        '<em>?</em>) : « à côté de » désigne seulement la case au-dessus, en dessous, à gauche ou à droite dans\n'
        'la même pièce, et le nord est en haut. Le bouton <em>Indice</em> place un suspect pour vous. Si ça ne\n'
        "colle toujours pas, écrivez-moi en indiquant l'affaire.</p>\n"
        '<h3>Quelles langues ?</h3>\n'
        "<p>Espagnol, anglais, allemand, français, italien et portugais. L'app suit la langue du téléphone et\n"
        'se change dans le menu.</p>'),
 'it': ('Assistenza',
        '<p class="resumen">Un problema, un caso che non torna o un\'idea? Scrivi a\n'
        '<a href="mailto:{correo}">{correo}</a> indicando il modello del tuo iPhone e la versione di iOS.\n'
        'Rispondo appena posso.</p>\n'
        '<h2>Domande frequenti</h2>\n'
        '<h3>Cosa è gratis?</h3>\n'
        '<p>I primi due capitoli (16 casi) e le tre sfide di oggi, ogni giorno. Il Club dei Detective include '
        'l’archivio dei giorni precedenti e tutti i sedici capitoli.</p>\n'
        "<h3>Come disdico l'abbonamento?</h3>\n"
        '<p>Su iPhone: <em>Impostazioni → il tuo nome → Abbonamenti → Crimenoku</em>. Controlla data di rinnovo e '
        'condizioni di eventuali prove. Disdici almeno 24 ore prima della fine del periodo per evitare il '
        'rinnovo.</p>\n'
        '<h3>Ho cambiato iPhone e non ho più il Club</h3>\n'
        '<p>Apri la schermata del Club e tocca <em>Ripristina acquisti</em>, con lo stesso Account Apple.</p>\n'
        '<h3>Ho perso i progressi</h3>\n'
        '<p>I progressi sono salvati solo sul dispositivo: non passano a un nuovo telefono e non si recuperano\n'
        "dopo aver eliminato l'app. L'abbonamento invece si recupera con <em>Ripristina acquisti</em>.</p>\n"
        '<h3>Un caso sembra senza soluzione</h3>\n'
        "<p>Ogni caso ha un'unica soluzione che si deduce senza tirare a indovinare. Rileggi le regole\n"
        '(pulsante <em>?</em>): «accanto a» è solo la casella sopra, sotto, a sinistra o a destra nella stessa\n'
        'stanza, e il nord è in alto. Il pulsante <em>Indizio</em> sistema un sospettato al posto tuo. Se\n'
        'ancora non torna, scrivimi dicendomi quale caso è.</p>\n'
        '<h3>In che lingue è?</h3>\n'
        '<p>Spagnolo, inglese, tedesco, francese, italiano e portoghese. Segue la lingua del telefono e si\n'
        'può cambiare dal menu.</p>'),
 'pt-BR': ('Suporte',
           '<p class="resumen">Algum problema, um caso que não fecha ou uma ideia? Escreva para\n'
           '<a href="mailto:{correo}">{correo}</a> e diga o modelo do seu iPhone e a versão do iOS. Respondo\n'
           'assim que der.</p>\n'
           '<h2>Perguntas frequentes</h2>\n'
           '<h3>O que é grátis?</h3>\n'
           '<p>Os dois primeiros capítulos (16 casos) e os três desafios de hoje, todos os dias. O Clube dos Detetives '
           'inclui o arquivo de dias anteriores e os dezesseis capítulos completos.</p>\n'
           '<h3>Como cancelo a assinatura?</h3>\n'
           '<p>No iPhone: <em>Ajustes → seu nome → Assinaturas → Crimenoku</em>. Consulte a data de renovação e as '
           'condições de qualquer teste disponível. Cancele pelo menos 24 horas antes do fim do período para evitar a '
           'renovação.</p>\n'
           '<h3>Troquei de iPhone e fiquei sem o Clube</h3>\n'
           '<p>Abra a tela do Clube e toque em <em>Restaurar compras</em>, com a mesma Conta Apple.</p>\n'
           '<h3>Perdi meu progresso</h3>\n'
           '<p>O progresso fica guardado só no aparelho: não vai para um celular novo nem volta depois de apagar\n'
           'o app. A assinatura, sim, volta com <em>Restaurar compras</em>.</p>\n'
           '<h3>Acho que um caso não tem solução</h3>\n'
           '<p>Todo caso tem uma única solução, que se deduz sem chutar. Releia as regras (botão <em>?</em>):\n'
           '“junto a” é só a casa de cima, de baixo, da esquerda ou da direita dentro do mesmo aposento, e o\n'
           'norte fica em cima. O botão <em>Pista</em> posiciona um suspeito para você. Se ainda assim não\n'
           'fechar, me escreva dizendo qual é o caso.</p>\n'
           '<h3>Em quais idiomas está?</h3>\n'
           '<p>Espanhol, inglês, alemão, francês, italiano e português. Segue o idioma do celular e pode ser\n'
           'trocado no menu.</p>')}

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
