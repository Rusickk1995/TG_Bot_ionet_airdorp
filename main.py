import telebot
from telebot import types

TOKEN = '7085195061:AAFYKdvovPj1g2-0D7_WCpKnZlxrU7fOmCI'

bot = telebot.TeleBot(TOKEN)

chat_states = {}

# Словарь для хранения соответствий текста кнопок и путей к изображениям
button_image_paths = {
    "Explanation of Work Status": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Обьяснение Статуса Работника": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Роз'яснення статусу працівника": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Explication du statut de l’employé": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Erläuterung des Status des Mitarbeiters": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Explicación de la situación del empleado": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Penjelasan status karyawan": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Kesilapan Yang Mungkin": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Giải thích về tình trạng của nhân viên": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "従業員のステータスの説明": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "कर्मचारी की स्थिति का स्पष्टीकरणं": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Paliwanag sa katayuan ng empleyado": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "직원의 상태에 대한 설명": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "對員工身份的解釋": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Explicação do estatuto do trabalhador": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Çalışanın durumunun açıklanması": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Wyjaśnienie statusu pracownika": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Spiegazione dello status del dipendente": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Explicarea statutului angajatului": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",
    "Uitleg over het statuut van de werknemer": r"C:\Users\slapa\Downloads\Снимок экрана 2024-03-19 122637.png",

}
docs_links = {
    "Russia": "https://io-russian-net.gitbook.io/io.net-russian-docs",
    "Ukraine": "https://io-net-ukrainian-docs.gitbook.io/untitled",
    "English": "https://developers.io.net/docs/overview",
    "French": "https://io-net-francais-docs.gitbook.io/untitled",
    "German": "https://io-net-deutch-docs.gitbook.io/untitled/erste-schritte/ueberblick",
    "Spanish": "https://io-net-spanish-docs.gitbook.io/io.net-spanish-docs",
    "Indonesian": "https://io-net-indonesian-docs.gitbook.io/untitled",
    "Vietnamese": "https://io-net-vietnamese-docs.gitbook.io/untitled",
    "Japan": "https://io-net-japanese-docs.gitbook.io/io.net-japanese-docs",
    "China": "https://io-net-china.gitbook.io/untitled/",
    "Italian": "https://io-net-italian.gitbook.io/docs/",
    "Turkish": "https://io-net-turkish.gitbook.io/io.net-turkish-docs/"
    # Добавьте другие языки и ссылки по аналогии
}


def send_docs_link(message):
    chat_id = message.chat.id
    selected_language = chat_states.get(chat_id, "Russia")  # Используйте язык по умолчанию, если язык не выбран

    if selected_language in docs_links:
        bot.send_message(chat_id, docs_links[selected_language])
    else:
        bot.send_message(chat_id, "Извините, ссылка на документацию для выбранного языка не найдена.")


@bot.message_handler(func=lambda message: message.text in ["Mac", "Windows", "Linux", "Explanation of Work Status",
                                                           "Обьяснение Статуса Работника",
                                                           "Роз'яснення статусу працівника",
                                                           "Explication du statut de l’employé",
                                                           "Erläuterung des Status des Mitarbeiters",
                                                           "Explicación de la situación del empleado",
                                                           "Penjelasan status karyawan", "Kesilapan Yang Mungkin",
                                                           "Giải thích về tình trạng của nhân viên",
                                                           "従業員のステータスの説明",
                                                           "कर्मचारी की स्थिति का स्पष्टीकरणं",
                                                           "Paliwanag sa katayuan ng empleyado", "맥", "윈도우", "리눅스",
                                                           "직원의 상태에 대한 설명", "對員工身份的解釋",
                                                           "Explicação do estatuto do trabalhador",
                                                           "Çalışanın durumunun açıklanması",
                                                           "Wyjaśnienie statusu pracownika",
                                                           "Spiegazione dello status del dipendente",
                                                           "Explicarea statutului angajatului",
                                                           "Uitleg over het statuut van de werknemer"])
def handle_buttons(message):
    chat_id = message.chat.id

    # Получение языка для текущего чата
    selected_language = chat_states.get(chat_id, "English")  # Если язык не найден, используется английский по умолчанию

    button_text = message.text
    photo_path = button_image_paths.get(button_text)

    if photo_path:
        with open(photo_path, 'rb') as photo:
            bot.send_photo(chat_id, photo)

    descriptions = {
        "English": {
            "Windows": "https://www.youtube.com/watch?v=U-FenqHlfuk",
            "Mac": "https://www.youtube.com/watch?v=vEmSL4bXEAs",
            "Linux": "Soon video...",
            "Explanation of Work Status": """ Explanation of each term of your worker 

1) Running - This status means that everything is set up correctly and everything is functioning.
2) Paused - This status indicates that you have manually paused or disabled the node.
3) Inactive - This status means that your node is unable to connect to the platform due to network issues, security settings, or other technical problems. You may have temporarily stopped your node, or the platform may have automatically stopped it due to inactivity or other factors.
4) Failed - This status means that there were errors encountered while starting your node, preventing successful launch. Insufficient resources such as allocated memory, CPU time, or other resources may be causing issues. Network problems may hinder connection to the platform or other services, leading to failures during startup.
5) Terminated - This status means that your node has been interrupted or terminated. For example, if you're running it on your computer and your computer goes to sleep or encounters a blue screen or Windows updates, you'll receive this error.
6) Unsupported - This status indicates that your node or its current configuration is not supported by the io.net platform. (Supported devices can be viewed here - https://developers.io.net/docs/supported-devices)
7) Blocked - This status means that your node has been blocked on the io.net platform. This could be caused by various reasons - contact Discord support - https://discord.gg/ionetofficial
8) Restart Required - This status means that a restart of your node is necessary due to changes in the system.
9) Idle - Your node is looking for work. """

        },
        "Russia": {
            "Windows": "Скоро...",
            "Mac": "Скоро...",
            "Linux": "Описание для Linux",
            "Обьяснение Статуса Работника": """ Разъяснение каждого термина Вашего работника, 
1) Running - Этот статус означает, что у вас всё установлено правильно и всё работает.
2) Paused- Этот статус означает, что вы вручную приостановили или отключили узел.
3) Inactive - Этот статус означает, что вашему узлу не удается подключиться к платформе из-за проблем сети, настройками безопасности или другими техническими проблемами. Возможно, вы временно остановили свой узел, или платформа автоматически остановила его из-за неактивности или других факторов. 
4) Failed - Этот статус означает, что у вас возникли ошибки  при запуске вашего узла, которые препятствовали успешному запуску. Возможно, для запуска вашего узла недостаточно ресурсов, таких как выделенная память, время ЦП или другие ресурсы.  Проблемы с сетью могут помешать установлению соединения с платформой или другими службами, что приводит к сбоям при запуске.
5) Terminated - Этот статус означает, что ваш узел был прерван или завершен. Например, если вы устанавливаете его на свой компьютер, и ваш компьютер переходит в режим сна или сталкивается с синим экраном или обновлениями Windows, вы получите эту ошибку.
6) Unsupported - Статус  указывает на то, что ваш узел или его текущая конфигурация не поддерживается платформой io.net. (Поддерживаемые устройства смотреть здесь - https://developers.io.net/docs/supported-devices)
7) Blocked- Статус означает, что ваш узел был заблокирован на платформе io.net . Это может быть вызвано различными причинами - обратиться в службу поддержки Discord - https://discord.gg/ionetofficial
8) Restart Required - Статус  означает, что необходим перезапуск вашего узла из-за каких-либо изменений в системе.
9) Idle - Ваш узел ищет работу.
     """
        },
        "Ukraine": {
            "Windows": "https://www.youtube.com/watch?v=vz5-618wAYs",
            "Mac": "https://www.youtube.com/watch?v=y2tg3j3i2VQ",
            "Linux": "Незабаром відео ...",
            "Роз'яснення статусу працівника": """ Роз'яснення кожного терміну вашого працівника
1) Running - Цей статус означає, що у вас все встановлено правильно і все працює.
2) Paused - Цей статус означає, що ви вручну призупинили або відключили вузол.
3) Inactive - Цей статус означає, що вашому вузлу не вдається підключитися до платформи через проблеми мережі, налаштування безпеки або інші технічні проблеми. Можливо, ви тимчасово призупинили свій вузол, або платформа автоматично призупинила його через неактивність або інші фактори.
4) Failed - Цей статус означає, що у вас виникли помилки при запуску вашого вузла, які перешкоджали успішному запуску. Можливо, для запуску вашого вузла не вистачає ресурсів, таких як виділена пам'ять, час ЦП або інші ресурси. Проблеми з мережею можуть заважати встановленню з'єднання з платформою або іншими службами, що призводить до збоїв при запуску.
5) Terminated - Цей статус означає, що ваш вузол був перерваний або завершений. Наприклад, якщо ви встановлюєте його на свій комп'ютер, і ваш комп'ютер переходить в режим сну або стикається з синім екраном або оновленнями Windows, ви отримаєте цю помилку.
6) Unsupported - Статус вказує на те, що ваш вузол або його поточна конфігурація не підтримується платформою io.net. (Підтримувані пристрої див. тут - https://developers.io.net/docs/supported-devices)
7) Blocked - Статус означає, що ваш вузол був заблокований на платформі io.net. Це може бути викликано різними причинами - зверніться до служби підтримки Discord - https://discord.gg/ionetofficial
8) Restart Required - Статус означає, що необхідний перезапуск вашого вузла через які-небудь зміни в системі.
9) Idle - Ваш вузол шукає роботу.    """
        },
        "French": {
            "Windows": "https://youtu.be/qjgBeg0GsQA?si=563aJ3zWnVa1SM0v",
            "Mac": "https://www.youtube.com/watch?v=3mljYOoId4Q",
            "Linux": """Bientôt, il y aura une vidéo...

Lien: https://io-net-francais-docs.gitbook.io/untitled/guide-dinstallation-fourniture/installation-sur-ubuntu """,
            "Explication du statut de l’employé": """ Explication de chaque terme de votre employé
1) Running - Ce statut signifie que tout est correctement installé et fonctionne.
2) Paused - Ce statut signifie que vous avez mis en pause ou arrêté manuellement le nœud.
3) Inactive - Ce statut signifie que votre nœud ne parvient pas à se connecter à la plateforme en raison de problèmes de réseau, de paramètres de sécurité ou d'autres problèmes techniques. Il se peut que vous ayez temporairement arrêté votre nœud, ou que la plateforme l'ait automatiquement arrêté en raison d'une inactivité ou d'autres facteurs.
4) Failed - Ce statut signifie que des erreurs sont survenues lors du démarrage de votre nœud, empêchant un démarrage réussi. Il se peut que les ressources nécessaires au démarrage de votre nœud, telles que la mémoire allouée, le temps CPU ou d'autres ressources, soient insuffisantes. Les problèmes de réseau peuvent également empêcher la connexion à la plateforme ou à d'autres services, entraînant des échecs de démarrage.
5) Terminated - Ce statut signifie que votre nœud a été interrompu ou arrêté. Par exemple, si vous l'installez sur votre ordinateur et que celui-ci passe en mode veille, rencontre un écran bleu ou effectue des mises à jour Windows, vous recevrez cette erreur.
6) Unsupported - Ce statut indique que votre nœud ou sa configuration actuelle n'est pas prise en charge par la plateforme io.net. Voir les appareils pris en charge ici - https://developers.io.net/docs/supported-devices
7) Blocked - Ce statut signifie que votre nœud a été bloqué sur la plateforme io.net. Cela peut être dû à diverses raisons - veuillez contacter le support Discord - https://discord.gg/ionetofficial.
8) Restart Required - Ce statut signifie qu'un redémarrage de votre nœud est nécessaire en raison de modifications apportées au système.
9) Idle - Votre nœud recherche du travail.

Ces traductions devraient vous aider à mieux comprendre chaque terme en français."""
        },
        "German": {
            "Windows": "https://www.youtube.com/watch?v=SDk3Mhg0VN4",
            "Mac": "https://www.youtube.com/watch?v=Ssq-Whf_CaY",
            "Linux": "Beschreibung für Linux",
            "Erläuterung des Status des Mitarbeiters": """Erläuterung der einzelnen Begriffe Ihres Mitarbeiters
1) Running - Dieser Status bedeutet, dass alles korrekt installiert ist und alles funktioniert.
2) Paused - Dieser Status bedeutet, dass Sie den Knoten manuell angehalten oder deaktiviert haben.
3) Inactive - Dieser Status bedeutet, dass Ihr Knoten keine Verbindung zur Plattform herstellen kann, aufgrund von Netzwerkproblemen, Sicherheitseinstellungen oder anderen technischen Problemen. Möglicherweise haben Sie Ihren Knoten vorübergehend angehalten, oder die Plattform hat ihn aufgrund von Inaktivität oder anderen Faktoren automatisch angehalten.
4) Failed - Dieser Status bedeutet, dass beim Starten Ihres Knotens Fehler aufgetreten sind, die einen erfolgreichen Start verhindert haben. Möglicherweise fehlen die für den Start Ihres Knotens erforderlichen Ressourcen wie zugewiesener Speicher, CPU-Zeit oder andere Ressourcen. Netzwerkprobleme können ebenfalls dazu führen, dass keine Verbindung zur Plattform oder anderen Diensten hergestellt werden kann, was zu Startfehlern führt.
5) Terminated - Dieser Status bedeutet, dass Ihr Knoten unterbrochen oder beendet wurde. Wenn Sie ihn beispielsweise auf Ihrem Computer installieren und Ihr Computer in den Ruhezustand wechselt oder auf einen blauen Bildschirm stößt oder Windows-Updates durchführt, erhalten Sie diesen Fehler.
6) Unsupported - Dieser Status zeigt an, dass Ihr Knoten oder seine aktuelle Konfiguration von der Plattform io.net nicht unterstützt wird. Unterstützte Geräte finden Sie hier - https://developers.io.net/docs/supported-devices
7) Blocked - Dieser Status bedeutet, dass Ihr Knoten auf der Plattform io.net blockiert wurde. Dies kann verschiedene Gründe haben - wenden Sie sich an den Discord-Support - https://discord.gg/ionetofficial.
8) Restart Required - Dieser Status bedeutet, dass ein Neustart Ihres Knotens aufgrund von Änderungen im System erforderlich ist.
9) Idle - Ihr Knoten sucht nach Arbeit. """

        },
        "Arabic": {
            "Windows": "الوصف لنظام التشغيل ويندوز",
            "Mac": "الوصف لنظام التشغيل ماك",
            "Linux": "الوصف لنظام التشغيل لينكس",
            "Возможные Ошибки": "حدث خطأ. الرجاء المحاولة مرة أخرى لاحقًا."
        },
        "Spanish": {
            "Windows": "Descripción para Windows",
            "Mac": "https://www.youtube.com/watch?v=MK0msOXVPp4",
            "Linux": "Descripción para Linux",
            "Explicación de la situación del empleado": """Explicación de cada término de su empleado
1) Running - Este estado significa que todo está instalado correctamente y funcionando.
2) Paused - Este estado significa que ha pausado o desconectado manualmente el nodo.
3) Inactive - Este estado significa que su nodo no puede conectarse a la plataforma debido a problemas de red, configuraciones de seguridad u otros problemas técnicos. Es posible que haya detenido temporalmente su nodo, o que la plataforma lo haya detenido automáticamente debido a la inactividad u otros factores.
4) Failed - Este estado significa que hubo errores al iniciar su nodo, lo que impidió un inicio exitoso. Puede ser que no haya suficientes recursos para iniciar su nodo, como memoria asignada, tiempo de CPU u otros recursos. Los problemas de red también pueden evitar la conexión a la plataforma u otros servicios, lo que provoca fallos al iniciar.
5) Terminated - Este estado significa que su nodo ha sido interrumpido o finalizado. Por ejemplo, si lo está instalando en su computadora y esta entra en modo de suspensión, se encuentra con una pantalla azul o realiza actualizaciones de Windows, recibirá este error.
6) Unsupported - Este estado indica que su nodo o su configuración actual no son compatibles con la plataforma io.net. Dispositivos compatibles pueden ser vistos aquí - https://developers.io.net/docs/supported-devices
7) Blocked - Este estado significa que su nodo ha sido bloqueado en la plataforma io.net. Esto puede deberse a diversas razones; póngase en contacto con el soporte de Discord - https://discord.gg/ionetofficial.
8) Restart Required - Este estado significa que es necesario reiniciar su nodo debido a cambios en el sistema.
9) Idle - Su nodo está buscando trabajo. """

        },
        "Indonesian": {
            "Windows": "Deskripsi untuk Windows",
            "Mac": "https://www.youtube.com/watch?v=7_-FCxH3TQ0&feature=youtu.be",
            "Linux": "Deskripsi untuk Linux",
            "Penjelasan status karyawan": """ Penjelasan setiap istilah karyawan Anda, 
1) Running - Status ini berarti bahwa semua sudah terinstal dengan benar dan semuanya berjalan.
2) Paused - Status ini berarti bahwa Anda secara manual menghentikan atau menonaktifkan node.
3) Inactive - Status ini berarti bahwa node Anda tidak dapat terhubung ke platform karena masalah jaringan, pengaturan keamanan, atau masalah teknis lainnya. Mungkin Anda telah sementara menghentikan node Anda, atau platform secara otomatis menghentikannya karena tidak aktif atau faktor lain.
4) Failed - Status ini berarti ada kesalahan saat memulai node Anda, yang mencegah dimulainya dengan sukses. Mungkin ada tidak cukup sumber daya untuk memulai node Anda, seperti memori yang dialokasikan, waktu CPU, atau sumber daya lainnya. Masalah jaringan juga dapat mencegah koneksi ke platform atau layanan lain, menyebabkan kegagalan saat memulai.
5) Terminated - Status ini berarti node Anda telah dihentikan atau selesai. Misalnya, jika Anda menginstalnya di komputer Anda dan komputer Anda masuk ke mode tidur, mengalami layar biru, atau melakukan pembaruan Windows, Anda akan menerima kesalahan ini.
6) Unsupported - Status ini menunjukkan bahwa node atau konfigurasi saat ini tidak didukung oleh platform io.net. Perangkat yang didukung dapat dilihat di sini - https://developers.io.net/docs/supported-devices
7) Blocked - Status ini berarti node Anda telah diblokir di platform io.net. Ini bisa disebabkan oleh berbagai alasan - hubungi dukungan Discord - https://discord.gg/ionetofficial.
8) Restart Required - Status ini berarti node Anda perlu di-restart karena ada perubahan dalam sistem.
9) Idle - Node Anda sedang mencari pekerjaan.

Ini adalah terjemahan ke dalam bahasa Indonesia dari setiap istilah."""
        },
        "Malay": {
            "Windows": "Penerangan untuk Windows",
            "Mac": "Penerangan untuk Mac",
            "Linux": "Penerangan untuk Linux",
            "Kesilapan Yang Mungkin": """ Penjelasan setiap penggal pekerja anda,
1) Running - Stèt sa vle di ke tout enstalasyon ou kòrèkteman ak tout bagay ap fonksyone.
2) Paused - Stèt sa vle di ke ou menm ki sispann oswa koupe nod la a mannyèlman.
3) Inactive - Stèt sa vle di ke nod ou pa ka konekte nan platfòm la akòz pwoblèm rezo, anviwònman sekirite, oswa lòt pwoblèm teknik. Ou ka te sispann nod ou tanperèman, oswa platfòm la ka sispann li otomatikman akoz nanaktivite oswa lòt faktè yo.
4) Failed - Stèt sa vle di ke gen erè lè ou lanse nod ou a ki anpeche li lanse siksè. Li ka gen pou pa ase resous pou lanse nod ou a, tankou memwa aloue, tan CPU, oswa lòt resous. Pwoblèm rezo yo ka tou bloke koneksyon nan platfòm la oswa lòt sèvis, ki mennen nan echèk lanseman.
5) Terminated - Stèt sa vle di ke nod ou te entèrompu oswa fini. Pou egzanp, si ou enstale li sou òdinatè ou ak òdinatè ou ale nan mod sommeil, rankontre yon ekran ble, oswa fè mizajou Windows, ou pral resevwa erè sa a.
6) Unsupported - Stèt sa endike ke nod ou oswa konfigirasyon li kounye a pa sipòte pa platfòm io.net. (Peranti yang disokong boleh dilihat di sini - https://developers.io.net/docs/supported-devices)
7) Blocked - Stèt sa vle di ke nod ou te blòke sou platfòm io.net. Sa ka kòz pa divès rezon - kontakte sipò Discord - https://discord.gg/ionetofficial.
8) Restart Required - Stèt sa vle di ke yon rekòmansman nan nod ou nesesè paske gen chanjman nan sistèm la.
9) Idle - Nod ou ap chèche travay. """

        },
        "Vietnamese": {
            "Windows": "https://www.youtube.com/watch?v=w518o2PU1lU",
            "Mac": "Mô tả cho Mac",
            "Linux": "Mô tả cho Linux",
            "Giải thích về tình trạng của nhân viên": """ Giải thích từng nhiệm kỳ của nhân viên

1) Running - Trạng thái này có nghĩa là mọi thứ đã được cài đặt đúng và đang hoạt động.
2) Paused - Trạng thái này có nghĩa là bạn đã tạm dừng hoặc tắt nút mạng một cách thủ công.
3) Inactive - Trạng thái này có nghĩa là nút của bạn không thể kết nối với nền tảng do sự cố mạng, cấu hình bảo mật hoặc các vấn đề kỹ thuật khác. Có thể bạn đã tạm dừng nút của mình tạm thời, hoặc nền tảng đã dừng nó tự động do không hoạt động hoặc các yếu tố khác.
4) Failed - Trạng thái này có nghĩa là đã xảy ra lỗi khi khởi động nút của bạn, ngăn cản việc khởi động thành công. Có thể không đủ tài nguyên để khởi động nút của bạn, như bộ nhớ được cấp phát, thời gian CPU hoặc các tài nguyên khác. Các vấn đề mạng cũng có thể ngăn cản kết nối đến nền tảng hoặc dịch vụ khác, dẫn đến lỗi khi khởi động.
5) Terminated - Trạng thái này có nghĩa là nút của bạn đã bị gián đoạn hoặc kết thúc. Ví dụ, nếu bạn cài đặt nó trên máy tính của mình và máy tính của bạn chuyển sang chế độ ngủ, gặp màn hình xanh hoặc cập nhật Windows, bạn sẽ nhận được lỗi này.
6) Unsupported - Trạng thái này cho biết nút hoặc cấu hình hiện tại của bạn không được hỗ trợ bởi nền tảng io.net. Thiết bị được hỗ trợ có thể xem tại đây - https://developers.io.net/docs/supported-devices
7) Blocked - Trạng thái này có nghĩa là nút của bạn đã bị chặn trên nền tảng io.net. Điều này có thể do nhiều nguyên nhân khác nhau - liên hệ với dịch vụ hỗ trợ Discord - https://discord.gg/ionetofficial.
8) Restart Required - Trạng thái này có nghĩa là cần phải khởi động lại nút của bạn do có thay đổi trong hệ thống.
9) Idle - Nút của bạn đang tìm kiếm công việc."""
        },
        "Japan": {
            "Windows": "Windows の説明",
            "Mac": "https://www.youtube.com/watch?v=gw8tm3cW3Y0",
            "Linux": "Linux の説明",
            "従業員のステータスの説明": """従業員の各学期の説明
1) 実行中 - このステータスは、すべてが正しく設定され、すべてが動作していることを意味します。
2) 一時停止中 - このステータスは、手動でノードを一時停止またはオフにしたことを意味します。
3) 無効 - このステータスは、ノードがネットワークの問題、セキュリティ設定、またはその他の技術的な問題により、プラットフォームに接続できないことを意味します。一時的にノードを停止した可能性がありますし、プラットフォームが非アクティブまたはその他の要因により自動的に停止した可能性もあります。
4) 失敗 - このステータスは、ノードの起動時に成功しないエラーが発生したことを意味します。ノードを起動するためのリソースが不足している可能性があります。例えば、割り当てられたメモリ、CPU時間、または他のリソースが不足している可能性があります。ネットワークの問題が、プラットフォームや他のサービスとの接続に支障をきたし、起動時の障害につながる可能性があります。
5) 終了 - このステータスは、ノードが中断または終了したことを意味します。例えば、ノードをコンピューターにインストールし、コンピューターがスリープモードに入ったり、ブルースクリーンエラーに遭遇したり、Windowsの更新を行ったりすると、このエラーが発生します。
6) サポートされていない - このステータスは、ノードまたはその現在の構成がio.netプラットフォームでサポートされていないことを示します。（サポートされているデバイスはこちらで確認できます - https://developers.io.net/docs/supported-devices）
7) ブロックされた - このステータスは、ノードがio.netプラットフォームでブロックされていることを意味します。これにはさまざまな理由があります - Discordサポートにお問い合わせください - https://discord.gg/ionetofficial
8) 再起動が必要 - このステータスは、システムの変更のためにノードを再起動する必要があることを意味します。
9) アイドル - ノードは作業を探しています。"""

        },
        "Hindi": {
            "Windows": "Windows के लिए विवरण",
            "Mac": "https://youtu.be/6_1VlnaVKAk",
            "Linux": "Linux के लिए विवरण",
            "कर्मचारी की स्थिति का स्पष्टीकरणं": """आपके कर्मचारी की प्रत्येक अवधि का स्पष्टीकरण
1) चल रहा है - इस स्थिति का मतलब है कि आपके पास सभी चीजें सही तरह से स्थापित हैं और सब कुछ काम कर रहा है।
2) ठहरा हुआ - यह स्थिति यह दर्शाती है कि आपने हस्तक्षेप करके नोड को रोक दिया है या बंद कर दिया है।
3) निष्क्रिय - यह स्थिति दर्शाती है कि आपके नोड को नेटवर्क समस्याओं, सुरक्षा सेटिंग्स या अन्य तकनीकी समस्याओं के कारण प्लेटफ़ॉर्म से कनेक्ट करने में असमर्थता है। संभावना है कि आपने अपने नोड को अस्थायी रूप से रोक दिया हो, या प्लेटफ़ॉर्म ने निष्क्रियता या अन्य कारणों के कारण इसे स्वचालित रूप से बंद कर दिया हो।
4) विफल - यह स्थिति दर्शाती है कि आपके नोड को प्रारंभ करते समय सफलतापूर्वक नहीं चला सका है क्योंकि त्रुटियां उत्पन्न हुईं हैं। आपके नोड को चलाने के लिए आवश्यक संसाधनों में कमी हो सकती है। उदाहरण के लिए, विशेष रूप से आवंटित मेमोरी, सीपीयू समय या अन्य संसाधनों की कमी हो सकती है। नेटवर्क समस्याएँ, प्लेटफ़ॉर्म या अन्य सेवाओं के साथ कनेक्टिविटी स्थापित करने में बाधा उत्पन्न कर सकती है, जो प्रारंभ करते समय असफलता का कारण बन सकती है।
5) समाप्त - यह स्थिति दर्शाती है कि आपका नोड विघटन या समाप्त हो गया है। उदाहरण के लिए, आप इसे अपने कंप्यूटर पर स्थापित कर रहे हैं, और आपका कंप्यूटर सो रहा है, या नीले स्क्रीन का सामना कर रहा है, या Windows के अपडेट के साथ सामना कर रहा है, तो आप इस त्रुटि को प्राप्त करेंगे।
6) असमर्थित - यह स्थिति दर्शाती है कि आपका नोड या उसकी वर्तमान कॉन्फ़िगरेशन io.net प्लेटफ़ॉर्म द्वारा समर्थित नहीं है। (समर्थित उपकरण यहाँ देखें - https://developers.io.net/docs/supported-devices)
7) अवरोधित - यह स्थिति दर्शाती है कि आपका नोड io.net प्लेटफ़ॉर्म पर अवरुद्ध कर दिया गया है। इसके कई कारण हो सकते हैं - Discord समर्थन सेवा से संपर्क करें - https://discord.gg/ionetofficial
8) पुनः आरंभ की आवश्यकता - यह स्थिति दर्शाती है कि सिस्टम में कोई भी परिवर्तन के कारण आपके नोड को पुनः आरंभ करने की आवश्यकता है।
9) खाली - आपका नोड काम खोज रहा है। """

        },
        "Filipino": {
            "Windows": "Deskripsyon para sa Windows",
            "Mac": "Deskripsyon para sa Mac",
            "Linux": "Deskripsyon para sa Linux",
            "Paliwanag sa katayuan ng empleyado": """Paliwanag sa bawat termino ng iyong empleyado
1) Patakbo - Ang status na ito ay nangangahulugang ang lahat ay maayos na na-install at gumagana.
2) Itinigil - Ang status na ito ay nangangahulugang ikaw ay nagpatahimik o nag-disconnect ng node nang mano-mano.
3) Hindi Aktibo - Ang status na ito ay nangangahulugang hindi makakonekta ang iyong node sa platform dahil sa mga isyu sa network, mga setting ng seguridad, o iba pang mga teknikal na problema. Maaring pansamantalang itinigil mo ang iyong node, o itinigil ito ng platform nang awtomatiko dahil sa hindi pagiging aktibo o iba pang mga kadahilanan.
4) Nabigo - Ang status na ito ay nangangahulugang mayroong mga error sa pagpapatakbo ng iyong node na humadlang sa tagumpay na pagpapatupad. Maaring kulangin ng resources tulad ng allocated memory, CPU time, o iba pang mga resources para sa pagpatakbo ng iyong node. Maaaring makaapekto ang mga isyu sa network sa pagtatayo ng koneksyon sa platform o iba pang mga serbisyo, na nagdudulot ng mga aberya sa pagpapatakbo.
5) Natapos - Ang status na ito ay nangangahulugang ang iyong node ay pinutol o tinapos. Halimbawa, kung ikaw ay nag-install nito sa iyong computer, at ang iyong computer ay pumapasok sa sleep mode o nagkakaroon ng blue screen o mga update sa Windows, makakatanggap ka ng ganitong error.
6) Hindi Suportado - Ang status na ito ay nagsasaad na ang iyong node o ang kasalukuyang configuration nito ay hindi sinusuportahan ng platform ng io.net. (Tingnan ang mga suportadong devices dito - https://developers.io.net/docs/supported-devices)
7) Nakabara - Ang status na ito ay nangangahulugang ang iyong node ay nabara sa platform ng io.net. Maaaring dulot ito ng iba't ibang mga dahilan - mangyaring makipag-ugnay sa suporta sa Discord - https://discord.gg/ionetofficial
8) Kinakailangang I-restart - Ang status na ito ay nangangahulugang kinakailangan ang restart ng iyong node dahil sa mga pagbabago sa sistema.
9) Idle - Ang iyong node ay naghahanap ng trabaho. """
        },
        "Korean": {
            "Windows": "Windows 설명",
            "Mac": "https://youtu.be/S3NuyElE4CQ?si=6QkltcYN7-C_OWCT",
            "Linux": "Linux 설명",
            "직원의 상태에 대한 설명": """직원의 각 임기에 대한 설명
 1) Running - 이 상태는 모든 것이 올바르게 설치되었고 모든 것이 작동 중임을 나타냅니다.
2) Paused - 이 상태는 수동으로 노드를 일시 정지하거나 중지했음을 의미합니다.
3) Inactive - 이 상태는 네트워크 문제, 보안 설정 또는 기타 기술적 문제로 인해 노드가 플랫폼에 연결되지 않는다는 것을 의미합니다. 일시적으로 노드를 중지했거나 플랫폼이 비활성 상태이거나 기타 요인으로 인해 자동으로 중지되었을 수 있습니다.
4) Failed - 이 상태는 노드를 시작할 때 발생한 오류로 인해 성공적인 시작을 방해했음을 나타냅니다. 할당된 메모리, CPU 시간 또는 기타 리소스가 부족할 수 있습니다. 네트워크 문제로 인해 플랫폼 또는 다른 서비스와의 연결 설정이 실패하여 시작 오류가 발생할 수 있습니다.
5) Terminated - 이 상태는 노드가 중지되거나 완료되었음을 나타냅니다. 예를 들어, 컴퓨터에 설치하고 컴퓨터가 절전 모드로 전환되거나 블루 스크린 또는 Windows 업데이트와 충돌하는 경우 이 오류가 발생할 수 있습니다.
6) Unsupported - 이 상태는 io.net 플랫폼에서 노드 또는 현재 구성이 지원되지 않음을 나타냅니다. (지원되는 장치는 여기에서 확인하십시오 - https://developers.io.net/docs/supported-devices)
7) Blocked - 이 상태는 io.net 플랫폼에서 노드가 차단되었음을 나타냅니다. 이는 다양한 이유로 인해 발생할 수 있습니다 - Discord 지원 서비스에 문의하십시오 - https://discord.gg/ionetofficial
8) Restart Required - 이 상태는 시스템 변경으로 인해 노드를 다시 시작해야 함을 나타냅니다.
9) Idle - 당신의 노드는 작업을 찾고 있습니다. """
        },
        "China": {
            "Windows": "Windows 的描述",
            "Mac": "Mac 的描述",
            "Linux": "Linux 的描述",
            "對員工身份的解釋": """對員工每個任期的解釋
1) Running - 這個狀態表示您的一切都正常安裝且一切運作正常。
2) Paused- 這個狀態表示您已手動暫停或停用節點。
3) Inactive - 這個狀態表示您的節點由於網絡問題、安全設置或其他技術問題而無法連接到平台。 可能您暫時停用了您的節點，或者由於無活動或其他因素，平台自動將其停用。
4) Failed - 這個狀態表示在啟動您的節點時出現錯誤，阻礙了成功的啟動。 可能由於資源不足，例如分配的內存、CPU時間或其他資源，導致您的節點無法啟動。 網絡問題可能導致無法與平台或其他服務建立連接，從而導致啟動失敗。
5) Terminated - 這個狀態表示您的節點已被終止或完成。 例如，如果您將其安裝在您的計算機上，並且您的計算機進入睡眠模式，或者遇到藍屏或Windows更新，您將收到此錯誤。
6) Unsupported - 此狀態表示 io.net 平台不支援您的節點或其當前配置。（請參閱支援的設備 - https://developers.io.net/docs/supported-devices）
7) Blocked- 此狀態表示您的節點已被 io.net 平台封鎖。 這可能是由各種原因引起的 - 請聯繫 Discord 支援服務 - https://discord.gg/ionetofficial
8) Restart Required - 此狀態表示由於系統中的某些更改，您的節點需要重新啟動。
9) Idle - 您的節點正在尋找工作。 """
        },
        "Portugal": {
            "Windows": "Descrição para Windows",
            "Mac": "https://youtu.be/T5i2hmF7BXc?si=6Ff2pHVyRTx-gV6H",
            "Linux": "Descrição para Linux",
            "Explicação do estatuto do trabalhador": """Explicação de cada termo do seu colaborador
1) Running - Este estado significa que tudo está instalado corretamente e tudo está funcionando.
2) Paused - Este estado significa que você pausou manualmente ou desativou o nó.
3) Inactive - Este estado significa que o seu nó não consegue se conectar à plataforma devido a problemas de rede, configurações de segurança ou outros problemas técnicos. É possível que você tenha temporariamente parado o seu nó, ou a plataforma o tenha parado automaticamente devido à inatividade ou outros fatores.
4) Failed - Este estado significa que ocorreram erros ao iniciar o seu nó, que impediram uma inicialização bem-sucedida. Pode ser que não haja recursos suficientes para iniciar o seu nó, como memória alocada, tempo de CPU ou outros recursos. Problemas de rede podem impedir a conexão com a plataforma ou outros serviços, resultando em falhas na inicialização.
5) Terminated - Este estado significa que o seu nó foi interrompido ou terminado. Por exemplo, se você o instalou no seu computador e o computador entra no modo de suspensão, se depara com uma tela azul ou atualizações do Windows, você receberá este erro.
6) Unsupported - Este estado indica que o seu nó ou a sua configuração atual não é suportada pela plataforma io.net. (Dispositivos suportados podem ser visualizados aqui - https://developers.io.net/docs/supported-devices)
7) Blocked - Este estado significa que o seu nó foi bloqueado na plataforma io.net. Isso pode ser causado por várias razões - entre em contato com o suporte no Discord - https://discord.gg/ionetofficial
8) Restart Required - Este estado significa que é necessário reiniciar o seu nó devido a alterações no sistema.
9) Idle - O seu nó está à procura de trabalho. """
        },
        "Turkish": {
            "Windows": "Windows için açıklama",
            "Mac": "https://youtu.be/7U-yrsdJZNw?si=HAmxFGsEph3wcJh4",
            "Linux": "Linux için açıklama",
            "Çalışanın durumunun açıklanması": """Çalışanınızın her döneminin açıklaması
1) Çalışıyor - Bu durum, her şeyin doğru bir şekilde kurulduğunu ve her şeyin çalıştığını gösterir.
2) Duraklatıldı - Bu durum, düğümü el ile duraklattığınızı veya devre dışı bıraktığınızı gösterir.
3) Etkin Değil - Bu durum, düğümünüzün platforma bağlanamadığını gösterir; ağ sorunları, güvenlik ayarları veya diğer teknik sorunlar nedeniyle. Geçici olarak düğümünüzü durdurmuş olabilirsiniz veya platformun etkin olmama veya diğer faktörler nedeniyle otomatik olarak durdurulmuş olabilir.
4) Başarısız - Bu durum, düğümünüzü başlatırken başarılı bir şekilde başlatmayı engelleyen hatalarla karşılaştığınızı gösterir. Düğümünüzü başlatmak için yeterli kaynak olmayabilir; ayrılan bellek, CPU süresi veya diğer kaynaklar gibi. Ağ sorunları, platform veya diğer hizmetlere bağlantı kurmayı engelleyerek başlatma sırasında arızalara neden olabilir.
5) Sonlandırıldı - Bu durum, düğümünüzün durdurulduğunu veya sonlandırıldığını gösterir. Örneğin, bilgisayarınıza kurduysanız ve bilgisayarınız uyku moduna geçer veya mavi ekran hatası alırsanız veya Windows güncellemeleriyle karşılaşırsanız, bu hatayı alırsınız.
6) Desteklenmiyor - Bu durum, düğümünüzün veya mevcut yapılandırmasının io.net platformu tarafından desteklenmediğini belirtir. (Desteklenen cihazlar için buraya bakın - https://developers.io.net/docs/supported-devices)
7) Engellendi - Bu durum, düğümünüzün io.net platformunda engellendiğini gösterir. Bu çeşitli nedenlerden kaynaklanabilir - Discord destek servisine başvurun - https://discord.gg/ionetofficial
8) Yeniden Başlatma Gerekli - Bu durum, sistemindeki değişiklikler nedeniyle düğümünüzü yeniden başlatmanız gerektiğini gösterir.
9) Boşta - Düğümünüz iş arıyor. """
        },
        "Poland": {
            "Windows": "Opis dla systemu Windows",
            "Mac": "Opis dla systemu Mac",
            "Linux": "Opis dla systemu Linux",
            "Wyjaśnienie statusu pracownika": """Wyjaśnienie każdego terminu Twojego pracownika
1) Uruchomiony - Ten status oznacza, że wszystko jest poprawnie zainstalowane i wszystko działa.
2) Wstrzymany - Ten status oznacza, że ręcznie wstrzymałeś lub wyłączyłeś węzeł.
3) Nieaktywny - Ten status oznacza, że twojemu węzłowi nie udało się połączyć z platformą z powodu problemów z siecią, ustawieniami bezpieczeństwa lub innymi problemami technicznymi. Możliwe, że tymczasowo zatrzymałeś swój węzeł, lub platforma automatycznie go zatrzymała z powodu braku aktywności lub innych czynników.
4) Nieudane - Ten status oznacza, że wystąpiły błędy podczas uruchamiania twojego węzła, które uniemożliwiły pomyślne uruchomienie. Może się zdarzyć, że brakuje zasobów do uruchomienia węzła, takich jak przydzielona pamięć, czas CPU lub inne zasoby. Problemy z siecią mogą uniemożliwić nawiązanie połączenia z platformą lub innymi usługami, co prowadzi do błędów podczas uruchamiania.
5) Zakończony - Ten status oznacza, że twój węzeł został przerwany lub zakończony. Na przykład, jeśli instalujesz go na swoim komputerze, a komputer przechodzi w tryb uśpienia lub natrafia na niebieski ekran lub aktualizacje systemu Windows, otrzymasz ten błąd.
6) Nieobsługiwane - Status ten oznacza, że twój węzeł lub jego obecna konfiguracja nie jest obsługiwana przez platformę io.net. (Sprawdź obsługiwane urządzenia tutaj - https://developers.io.net/docs/supported-devices)
7) Zablokowany - Ten status oznacza, że twój węzeł został zablokowany na platformie io.net. Może to być spowodowane różnymi przyczynami - skontaktuj się ze wsparciem Discord - https://discord.gg/ionetofficial
8) Wymagany restart - Ten status oznacza, że konieczny jest restart twojego węzła z powodu jakichkolwiek zmian w systemie.
9) Bezczynny - Twój węzeł szuka pracy. """
        },
        "Italian": {
            "Windows": "Descrizione per Windows",
            "Mac": "https://youtu.be/DBFiZvJOKeo?si=XfqZfNh0a5moAXa_",
            "Linux": "Descrizione per Linux",
            "Spiegazione dello status del dipendente": """Spiegazione di ogni termine del tuo dipendente
1) Running - Questo stato significa che tutto è installato correttamente e funziona.
2) Paused - Questo stato indica che hai messo in pausa o disattivato manualmente il nodo.
3) Inattivo - Questo stato indica che al tuo nodo non è possibile connettersi alla piattaforma a causa di problemi di rete, impostazioni di sicurezza o altri problemi tecnici. Potresti aver temporaneamente fermato il tuo nodo, o la piattaforma potrebbe averlo fermato automaticamente a causa di inattività o altri fattori.
4) Fallito - Questo stato indica che ci sono stati errori durante l'avvio del tuo nodo che hanno impedito un avvio corretto. Potrebbe non esserci abbastanza risorse disponibili per avviare il tuo nodo, come memoria allocata, tempo CPU o altre risorse. I problemi di rete possono impedire la connessione alla piattaforma o ad altri servizi, causando errori durante l'avvio.
5) Terminato - Questo stato indica che il tuo nodo è stato interrotto o terminato. Ad esempio, se lo installi sul tuo computer e il computer va in modalità standby, si verifica un errore dello schermo blu o vengono eseguiti gli aggiornamenti di Windows.
6) Non supportato - Questo stato indica che il tuo nodo o la sua configurazione attuale non sono supportati dalla piattaforma io.net. (Consulta i dispositivi supportati qui - https://developers.io.net/docs/supported-devices)
7) Bloccato - Questo stato indica che il tuo nodo è stato bloccato sulla piattaforma io.net. Ciò può essere causato da vari motivi - contattare il supporto su Discord - https://discord.gg/ionetofficial
8) Riavvio richiesto - Questo stato indica che è necessario riavviare il tuo nodo a causa di eventuali modifiche al sistema.
9) Inattivo - Il tuo nodo è in cerca di lavoro. """
        },
        "Romanian": {
            "Windows": "https://www.youtube.com/watch?v=KNdbnnlM5oQ",
            "Mac": "Descriere pentru Mac",
            "Linux": "Descriere pentru Linux",
            "Explicarea statutului angajatului": """Explicarea fiecărui termen al angajatului dvs
1) Running - Acest status indică faptul că totul este instalat corect și funcționează.
2) Paused - Acest status indică faptul că ați oprit manual sau ați pus în pauză nodul.
3) Inactiv - Acest status indică faptul că nodul dvs. nu poate fi conectat la platformă din cauza problemelor de rețea, setărilor de securitate sau altor probleme tehnice. Poate fi posibil să ați oprit temporar nodul sau platforma l-a oprit automat din cauza inactivității sau a altor factori.
4) Failed - Acest status indică faptul că au apărut erori la pornirea nodului dvs., care au împiedicat o pornire reușită. Este posibil să nu fie suficiente resurse disponibile pentru a porni nodul dvs., cum ar fi memoria alocată, timpul CPU sau alte resurse. Problemele de rețea pot împiedica conectarea la platformă sau la alte servicii, ceea ce duce la erori la pornire.
5) Terminat - Acest status indică faptul că nodul dvs. a fost întrerupt sau terminat. De exemplu, dacă îl instalați pe computerul dvs. și computerul intră în modul de hibernare, apare o eroare de ecran albastru sau sunt efectuate actualizări pentru Windows.
6) Unsupported - Acest status indică faptul că nodul dvs. sau configurația sa curentă nu este acceptată de platforma io.net. (Consultați dispozitivele acceptate aici - https://developers.io.net/docs/supported-devices)
7) Blocat - Acest status indică faptul că nodul dvs. a fost blocat pe platforma io.net. Acest lucru poate fi cauzat de diferite motive - contactați suportul pe Discord - https://discord.gg/ionetofficial
8) Este necesar restartul - Acest status indică faptul că este necesar să reporniți nodul dvs. din cauza unor modificări în sistem.
9) Idle - Nodul dvs. caută un loc de muncă. """
        },
        "Dutch": {
            "Windows": "Beschrijving voor Windows",
            "Mac": "Beschrijving voor Mac",
            "Linux": "Beschrijving voor Linux",
            "Uitleg over het statuut van de werknemer": """Toelichting op elke termijn van uw werknemer
1) Running - Deze status betekent dat alles correct is geïnstalleerd en werkt.
2) Paused - Deze status betekent dat je handmatig de node hebt gepauzeerd of uitgeschakeld.
3) Inactive - Deze status betekent dat uw node geen verbinding kan maken met het platform vanwege netwerkproblemen, beveiligingsinstellingen of andere technische problemen. Mogelijk hebt u uw node tijdelijk gestopt, of het platform heeft het automatisch gestopt vanwege inactiviteit of andere factoren.
4) Failed - Deze status betekent dat er fouten zijn opgetreden bij het opstarten van uw node die een succesvolle start hebben verhinderd. Het kan zijn dat er onvoldoende middelen beschikbaar zijn om uw node te starten, zoals toegewezen geheugen, CPU-tijd of andere bronnen. Netwerkproblemen kunnen voorkomen dat er verbinding wordt gemaakt met het platform of andere services, wat kan leiden tot fouten bij het opstarten.
5) Terminated - Deze status betekent dat uw node is onderbroken of beëindigd. Bijvoorbeeld, als u het op uw computer installeert en uw computer in de slaapstand gaat of wordt geconfronteerd met een blauw scherm of Windows-updates, krijgt u deze foutmelding.
6) Unsupported - Deze status geeft aan dat uw node of de huidige configuratie ervan niet wordt ondersteund door het io.net-platform. (Ondersteunde apparaten vindt u hier - https://developers.io.net/docs/supported-devices)
7) Blocked - Deze status betekent dat uw node is geblokkeerd op het io.net-platform. Dit kan verschillende redenen hebben - neem contact op met de Discord-ondersteuningsservice - https://discord.gg/ionetofficial
8) Restart Required - Deze status betekent dat een herstart van uw node nodig is vanwege wijzigingen in het systeem.
9) Idle - Uw node zoekt naar werk. """
        }

    }

    links = {
        "English": {
            "Windows": "https://developers.io.net/docs/installing-on-windows",
            "Mac": "https://developers.io.net/docs/installing-on-mac-os",
            "Linux": "https://developers.io.net/docs/installing-on-ubuntu",
            "Explanation of Work Status": None
        },

    }

    button_text = message.text
    description = descriptions.get(selected_language, {}).get(button_text, "No description available.")
    link = links.get(selected_language, {}).get(button_text)

    bot.send_message(chat_id, description)

    if link:
        bot.send_message(chat_id, "Link: " + link)


languages_to_use = {
    "English": ["Galxe", "Nodes", "Discord Role", "Docs", "Back"],
    "Russia": ["Galxe", "Нода", "Роли Discord", "Документы", "Назад"],
    "Ukraine": ["Galxe", "Нода", "Ролі Discord", "Документи", "Назад"],
    "French": ["Galxe", "Node", "Rôles Discord", "Documents", "Retour"],
    "German": ["Galxe", "Knoten", "Discord-Rollen", "Urkunden", "Zurück"],
    "Arabic": ["نشاط", "ترجمات", "عودة"],
    "Spanish": ["Galxe", "Nodo", "Roles de Discord", "Documentos", "Volver"],
    "Indonesian": ["Galxe", "Node", "Peran Discord", "Dokumen", "Kembali"],
    "Malay": ["Galxe", "Node", "Peran Discord", "Dokumen", "Kembali"],
    "Vietnamese": ["Galxe", "Nút", "Vai trò Discord", "Tài liệu", "Quay lại"],
    "Japan": ["Galxe", "ノード", "Discord の役割", "書類", "バック"],
    "Hindi": ["गॅलक्स", "नोड्स", "Vकलह भूमिकाएँ", "दस्तावेज़", "पीछे जाएं"],
    "Filipino": ["Galxe", "Node", "Mga Papel ng Discord", "Mga Dokumento", "Bumalik"],
    "Korean": ["갈스크", "노드", "디스코드 롤리", "문서", "뒤로가기"],
    "China": ["加爾克斯", "節點", "Discord 角色", "檔", "返回"],
    "Portugal": ["Galxe", "Nó", "Funções do Discord", "Documentação", "Voltar"],
    "Turkish": ["Galxe", "Düğme", "Discord Rolleri", "Evrak", "Geri"],
    "Poland": ["Galxe", "Węzeł", "Role Discorda", "Dokumentów", "Wstecz"],
    "Italian": ["Galxe", "Nodo", "Ruoli di Discord", "Documenti", "Indietro"],
    "Romanian": ["Galxe", "Nod", "Roluri Discord", "Documente", "Înapoi"],
    "Dutch": ["Galxe", "Knoop", "Discord-rollen", "Documenten", "Terug"],
}

back_button_texts = ["Back", "Назад", "Retour", "Zurück", "Volver", "Kembali", "Quay lại", "バック", "पीछे जाएं",
                     "Bumalik",
                     "뒤로가기", "返回", "Voltar", "Geri", "Wstecz", "Indietro", "Înapoi", "Terug"]

galxe_links = {
    "Galxe": "https://galxe.com/io.net",
    "ガルクス": "https://galxe.com/io.net",
    "गॅलक्स": "https://galxe.com/io.net",
    "加爾克斯": "https://galxe.com/io.net",
    "갈스크": "https://galxe.com/io.net",
}


def start(update, context):
    # Описание бота
    bot_description = "Добро пожаловать! Этот бот предоставляет доступ к документации по языкам и устройствам."

    # Отправляем описание бота
    update.message.reply_text(bot_description)

    # Отправляем кнопку старт
    start_button = types.KeyboardButton('/start')
    custom_keyboard = types.ReplyKeyboardMarkup([[start_button]], resize_keyboard=True)
    update.message.reply_text("Нажмите кнопку 'Старт', чтобы начать.", reply_markup=custom_keyboard)


@bot.message_handler(commands=['start'])
def start(message):
    # Получаем информацию о пользователе
    user = message.from_user
    username = user.username
    first_name = user.first_name

    # Формируем приветственное сообщение с использованием имени пользователя
    greeting_message = f"Hello, {first_name} ({username})!  I'm Bot io.net, providing comprehensive project information."

    # Описание бота
    bot_description = "Information on Discord Roles / Node Installation (Mac / Windows / Linux), troubleshooting errors, and more."

    # Отправляем приветственное сообщение
    bot.send_message(message.chat.id, greeting_message)

    # Отправляем описание бота
    bot.send_message(message.chat.id, bot_description)

    # Создаем клавиатуру с выбором языка
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    languages = list(languages_to_use.keys())[:25]
    buttons = [types.KeyboardButton(language) for language in languages]
    markup.add(*buttons)

    # Отправляем сообщение с предложением выбрать язык
    bot.send_message(message.chat.id, 'Choose your language:', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        chat_id = message.chat.id
        if message.text in languages_to_use:
            chat_states[chat_id] = message.text
            bot.send_message(chat_id, f'You have chosen a language: {message.text}')
            send_main_menu(message)
        elif message.text in back_button_texts:
            if chat_id in chat_states:
                del chat_states[chat_id]
            start(message)
        elif message.text == "Роли Discord" or message.text == "Ролі Discord":
            send_roles_info(message)
        elif message.text == "Rôles Discord":
            send_roles_info(message)
        elif message.text == "Discord-Rollen":
            send_roles_info(message)
        elif message.text == "Roles de Discord":
            send_roles_info(message)
        elif message.text == "Peran Discord":
            send_roles_info(message)
        elif message.text == "Peran Discord":
            send_roles_info(message)
        elif message.text == "Vai trò Discord":
            send_roles_info(message)
        elif message.text == "Discord の役割":
            send_roles_info(message)
        elif message.text == "Vकलह भूमिकाएँ":
            send_roles_info(message)
        elif message.text == "Mga Papel ng Discord":
            send_roles_info(message)
        elif message.text == "디스코드 롤리":
            send_roles_info(message)
        elif message.text == "Discord 角色":
            send_roles_info(message)
        elif message.text == "Funções do Discord":
            send_roles_info(message)
        elif message.text == "Discord Rolleri":
            send_roles_info(message)
        elif message.text == "Role Discorda":
            send_roles_info(message)
        elif message.text == "Ruoli di Discord":
            send_roles_info(message)
        elif message.text == "Roluri Discord":
            send_roles_info(message)
        elif message.text == "Discord-rollen":
            send_roles_info(message)
        elif message.text == "Discord Role":
            send_roles_info(message)
        elif message.text in galxe_links:
            send_galxe_link(message)
        elif message.text == "Düğme" or message.text == "節點" or message.text == "노드" or message.text == "Knoop" or message.text == "Nodes" or message.text == "Nó" or message.text == "Нода" or message.text == "Node" or message.text == "Knoten" or message.text == "ノード" or message.text == "نشاط" or message.text == "Nodo" or message.text == "Node" or message.text == "Nút" or message.text == "ノード" or message.text == "नोड्स" or message.text == "Node" or message.text == "Nodo" or message.text == "Nod" or message.text == "Nodo" or message.text == "Node" or message.text == "Węzeł" or message.text == "Nodo" or message.text == "Nod":
            send_nodes_menu(message)
        elif message.text == "Документи":
            send_docs_link(message)
        elif message.text == "Документы":
            send_docs_link(message)
        elif message.text == "Documents":
            send_docs_link(message)
        elif message.text == "Docs":
            send_docs_link(message)
        elif message.text == "Urkunden":
            send_docs_link(message)
        elif message.text == "Documentos":
            send_docs_link(message)
        elif message.text == "Dokumen":
            send_docs_link(message)
        elif message.text == "Tài liệu":
            send_docs_link(message)
        elif message.text == "書類":
            send_docs_link(message)
        elif message.text == "檔":
            send_docs_link(message)
        elif message.text == "Documenti":
            send_docs_link(message)
        elif message.text == "Evrak":
            send_docs_link(message)

        else:
            pass


def send_main_menu(message):
    chat_id = message.chat.id
    selected_language = chat_states.get(chat_id, "Russia")

    main_menu_messages = {
        "Russia": "Основное меню",
        "Ukraine": "Головне меню",
        "French": "Menu principal",
        "German": "Hauptmenü",
        "Arabic": "قائمة رئيسية",
        "Spanish": "Menú Principal",
        "Indonesian": "Menu Utama",
        "Malay": "Menu Utama",
        "Vietnamese": "Menu chính",
        "Japan": "メインメニュー",
        "Hindi": "मुख्य मेनू",
        "Filipino": "Pangunahing Menu",
        "Korean": "메인 메뉴",
        "China": "主功能表",
        "Portugal": "Menu Principal",
        "Turkish": "Ana Menü",
        "Poland": "Menu główne",
        "Italian": "Menu Principale",
        "Romanian": "Meniul principal",
        "Dutch": "Hoofdmenu",
    }

    main_menu_message = main_menu_messages.get(selected_language, "Main menu")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = languages_to_use[selected_language]
    markup.add(*buttons)

    bot.send_message(chat_id, main_menu_message, reply_markup=markup)


def send_roles_info(message):
    roles_info_russian = """На сервере существует 10 уровней ролей + Роли Модератора или Технического помощника:
1) Уровень 1 - Для получения этой роли вам нужно пройти верификацию на сервере Discord и подключить свой кошелек SOLANA в ветке #wallet-submission.
2) Уровень 2 - Для получения этой роли вам нужно участвовать в АМА мероприятиях (Каждую среду - время смотрите в Discord/События) или участвовать в розыгрышах от модераторов в разных каналах Discord.
3) Уровень 3+ (выдается исключительно командой) - Для получения этой роли вам нужно быть максимально активным и полезным участником на сервере Discord.
4) Уровень 4 (Амбассадор) - Для получения этой роли вам нужно помогать новичкам, взаимодействовать с их Twitter, создавать качественный контент (мемы, гайды, статьи, переводы, инфографику, видео и прочее).
5) Уровень 5-10 - Выдается в зависимости от вашей активности в проекте.

Также вы можете создать изображение на https://bc8.ai/ и отправить свой результат в Discord #made-witc-bc8.
    """
    roles_info_ukrainian = """На сервері існує 10 рівнів ролей + Ролі Модератора або Технічного помічника:
1) Рівень 1 - Для отримання цієї ролі вам потрібно пройти верифікацію на сервері Discord та підключити свій кошелек SOLANA в гілці #wallet-submission.
2) Рівень 2 - Для отримання цієї ролі вам потрібно брати участь в АМА заходах (Кожної середи - час дивіться у Discord/Події) або розіграшах від модераторів у різних каналах Discord.
3) Рівень 3+ (видається винятково командою) - Для отримання цієї ролі вам потрібно бути максимально активним та корисним учасником на сервері Discord.
4) Рівень 4 (Амбасадор) - Для отримання цієї ролі вам потрібно допомагати новачкам, взаємодіяти з їх Twitter, створювати якісний контент (меми, гайди, статті, переклади, інфографіку, відео та інше).
5) Рівень 5-10 - Видається залежно від вашої активності в проекті.

Також ви можете створити зображення на https://bc8.ai/ та відправити свій результат у Discord #made-witc-bc8.
    """
    roles_info_french = """Il y a un total de 10 - Rôles de niveau + Rôles de modérateur ou d'assistant technique sur le serveur:
1) Niveau 1 - Pour obtenir ce rôle, vous devez vous vérifier sur le serveur Discord et connecter votre portefeuille SOLANA dans la section #wallet-submission
2) Niveau 2 - Pour obtenir ce rôle, vous devez participer aux événements AMA (chaque mercredi - regardez l'heure dans Discord/Événements) ou aux tirages au sort organisés par les modérateurs dans différentes sections du Discord
3) Niveau 3+ (Attribué exclusivement par l'équipe) - Pour obtenir ce rôle, vous devez être très actif / utile sur le Discord
4) Niveau 4 (Ambassadeur) - Pour obtenir ce rôle, vous devez aider les nouveaux arrivants / interagir avec leur Twitter / créer du contenu de qualité (mèmes/guides/articles/traductions/infographies/vidéos, etc.)
5) Niveau 5 - 10 Est attribué en fonction de votre activité dans le projet
Vous pouvez également générer une image sur https://bc8.ai/ et envoyer votre résultat dans le Discord #made-witc-bc8
    """
    roles_info_german = """Auf dem Server gibt es insgesamt 10 - Tier-Rollen + Moderator- oder Techniker-Assistentenrollen
1) Tier 1 - Um diese Rolle zu erhalten, müssen Sie sich auf dem Discord-Server verifizieren und Ihre SOLANA-Brieftasche im Bereich #wallet-submission verbinden
2) Tier 2 - Um diese Rolle zu erhalten, müssen Sie an AMA-Veranstaltungen teilnehmen (jeden Mittwoch - die Uhrzeit finden Sie in Discord/Veranstaltungen) oder an Verlosungen von Moderatoren in verschiedenen Discord-Bereichen teilnehmen
3) Tier 3+ (Wird ausschließlich vom Team vergeben) - Um diese Rolle zu erhalten, müssen Sie im Discord maximal aktiv / nützlich sein
4) Tier 4 (Botschafter) - Um diese Rolle zu erhalten, müssen Sie Neulingen helfen / mit ihrem Twitter interagieren / hochwertigen Inhalt erstellen (Memes/Anleitungen/Artikel/Übersetzungen/Infografiken/Videos usw.)
5) Tier 5 - 10 Wird je nach Ihrer Aktivität im Projekt vergeben
Sie können auch ein Bild auf https://bc8.ai/ generieren und Ihr Ergebnis in Discord #made-witc-bc8 senden
    """
    roles_info_spanish = """En el servidor hay un total de 10 - Roles de Tier + Roles de moderador o asistente técnico
1) Tier 1 - Para obtener este rol, debes verificarte en el servidor de Discord y conectar tu billetera SOLANA en la sección #wallet-submission
2) Tier 2 - Para obtener este rol, debes participar en los eventos AMA (cada miércoles - consulta la hora en Discord/Eventos) o en sorteos de moderadores en diferentes secciones de Discord
3) Tier 3+ (Otorgado exclusivamente por el equipo) - Para obtener este rol, debes ser muy activo / útil en Discord
4) Tier 4 (Embajador) - Para obtener este rol, debes ayudar a los recién llegados / interactuar con su Twitter / crear contenido de calidad (memes/guías/artículos/traducciones/infografías/videos, etc.)
5) Tier 5 - 10 Se otorga según tu actividad en el proyecto
También puedes generar una imagen en https://bc8.ai/ y enviar tu resultado en Discord #made-witc-bc8
    """
    roles_info_indonesian = """ Secara total, terdapat 10 - Tier Roles + Roles Moderator atau Asisten Teknis di server
1) Tier 1 - Untuk mendapatkan peran ini, Anda harus melakukan verifikasi di server Discord dan menghubungkan dompet SOLANA Anda di bagian #wallet-submission
2) Tier 2 - Untuk mendapatkan peran ini, Anda harus berpartisipasi dalam acara AMA (setiap hari Rabu - lihat waktu di Discord/Acara) atau undian dari moderator di berbagai bagian Discord
3) Tier 3+ (Diberikan secara eksklusif oleh tim) - Untuk mendapatkan peran ini, Anda harus sangat aktif / berguna di Discord
4) Tier 4 (Duta Besar) - Untuk mendapatkan peran ini, Anda harus membantu pemula / berinteraksi dengan Twitter mereka / membuat konten berkualitas (meme/panduan/artikel/penerjemahan/infografis/video, dll.)
5) Tier 5 - 10 Diberikan berdasarkan aktivitas Anda dalam proyek
Anda juga dapat menghasilkan gambar di https://bc8.ai/ dan mengirimkan hasil Anda di Discord #made-witc-bc8
    """
    roles_info_malay = """ Secara keseluruhan, terdapat 10 - Peranan Tier + Peranan Moderator atau Pembantu Teknikal di dalam pelayan
1) Tier 1 - Untuk memperoleh peranan ini, anda perlu melakukan pengesahan di pelayan Discord dan menyambung dompet SOLANA anda di bahagian #wallet-submission
2) Tier 2 - Untuk memperoleh peranan ini, anda perlu mengambil bahagian dalam acara AMA (setiap hari Rabu - lihat waktu di Discord/Acara) atau cabutan bertuah dari moderator di pelbagai bahagian Discord
3) Tier 3+ (Diberikan secara eksklusif oleh pasukan) - Untuk memperoleh peranan ini, anda perlu sangat aktif / berguna di Discord
4) Tier 4 (Duta Besar) - Untuk memperoleh peranan ini, anda perlu membantu orang baru / berinteraksi dengan Twitter mereka / mencipta kandungan berkualiti (meme/panduan/artikel/penterjemahan/infografik/video, dan lain-lain)
5) Tier 5 - 10 Diberikan berdasarkan aktiviti anda dalam projek
Anda juga boleh menghasilkan gambar di https://bc8.ai/ dan menghantar keputusan anda di Discord #made-witc-bc8 """

    roles_info_vietnamese = """ Dưới tổng cộng, có 10 - Cấp Độ Vai trò + Vai trò của Quản trị viên hoặc Trợ lý Kỹ thuật trên máy chủ

Cấp Độ 1 - Để nhận được vai trò này, bạn cần xác minh trên máy chủ Discord và kết nối ví SOLANA của bạn trong phần #wallet-submission
Cấp Độ 2 - Để nhận được vai trò này, bạn cần tham gia sự kiện AMA (Mỗi thứ Tư - xem thời gian trên Discord/Sự kiện) hoặc bốc thăm may mắn từ các quản trị viên trong các phòng khác nhau trên Discord
Cấp Độ 3+ (Được cấp phát độc quyền bởi đội ngũ) - Để nhận được vai trò này, bạn cần hoạt động / hữu ích tối đa trên Discord
Cấp Độ 4 (Đại sứ) - Để nhận được vai trò này, bạn cần giúp đỡ người mới / tương tác với Twitter của họ / tạo ra nội dung chất lượng (hình meme/hướng dẫn/bài viết/dịch thuật/đồ họa thông tin/video và những thứ khác)
Cấp Độ 5 - 10 Được cấp phát dựa trên hoạt động của bạn trong dự án
Bạn cũng có thể tạo hình ảnh tại https://bc8.ai/ và gửi kết quả của bạn trong Discord #made-witc-bc8 """

    roles_info_japan = """ サーバーには、合計で10のティア役職とモデレーターまたはテクニカルアシスタント役職が存在します

ティア1 - この役職を取得するには、Discordサーバーで認証を行い、SOLANAウォレットを #wallet-submission で接続する必要があります
ティア2 - この役職を取得するには、AMAイベントに参加する必要があります（毎週水曜日 - 時間はDiscord/イベントで確認してください）またはDiscordのさまざまなチャンネルでモデレーターからの抽選に参加する必要があります
ティア3+（チームによってのみ付与） - この役職を取得するには、Discordで最大限に活動し/有用である必要があります
ティア4（アンバサダー） - この役職を取得するには、新規参加者に助言をし、彼らのTwitterと対話し、クオリティの高いコンテンツを作成する必要があります（ミーム/ガイド/記事/翻訳/インフォグラフィック/動画など）
ティア5 - 10 は、プロジェクトでの活動に応じて授与されます
また、 https://bc8.ai/ で画像を生成し、結果を Discord の #made-witc-bc8 に送信することもできます。"""

    roles_info_hindi = """ सार्वजनिक सर्वर पर कुल 10 - टियर रोल और मॉडरेटर या तकनीकी सहायक रोल होते हैं

टियर 1 - इस रोल को प्राप्त करने के लिए, आपको डिस्कॉर्ड सर्वर पर प्रमाणीकरण करना होगा और #wallet-submission शाखा में अपना SOLANA वॉलेट कनेक्ट करना होगा
टियर 2 - इस रोल को प्राप्त करने के लिए, आपको AMA इवेंट में भाग लेना होगा (हर बुधवार - समय Discord/घटनाओं में देखें) या डिस्कॉर्ड के विभिन्न शाखाओं में मॉडरेटरों के लक्ष्यों में भाग लेना होगा
टियर 3+ (केवल टीम द्वारा प्रदान किया जाता है) - इस रोल को प्राप्त करने के लिए, आपको Discord में सबसे अधिक सक्रिय / उपयोगी व्यक्ति होना चाहिए
टियर 4 (एम्बैसडर) - इस रोल को प्राप्त करने के लिए, आपको नए उपयोगकर्ताओं की मदद करनी होगी / उनके Twitter के साथ बातचीत करनी होगी / उच्च गुणवत्ता कंटेंट (मीम्स/गाइड/लेख/अनुवाद/इन्फोग्राफ़िक/वीडियो आदि) बनानी होगी
टियर 5 - 10 आपकी परियोजना में गतिविधि के आधार पर दिया जाता है
आप यहां चित्र उत्पन्न कर सकते हैं https://bc8.ai/ और अपने परिणाम को Discord #made-witc-bc8 में भेज सकते हैं। """

    roles_info_filipino = """ Sa kabuuan, mayroong 10 - Tier Roles + Moderator o Technical Assistant Roles sa server

Tier 1 - Upang makuha ang papel na ito, kailangan mong i-verify ang iyong sarili sa Discord server at ikonekta ang iyong SOLANA wallet sa branch na #wallet-submission
Tier 2 - Upang makuha ang papel na ito, kailangan mong lumahok sa mga AMA event (Tuwing Miyerkules - tingnan ang oras sa Discord/Events) o sumali sa mga raffle mula sa mga moderator sa iba't ibang branches ng Discord
Tier 3+ (Ipinapamahagi lamang ng team) - Upang makuha ang papel na ito, kailangan mong maging napaka-aktibo / kapaki-pakinabang sa Discord
Tier 4 (Embahador) - Upang makuha ang papel na ito, kailangan mong tulungan ang mga baguhan / makipag-ugnayan sa kanilang Twitter / lumikha ng magandang nilalaman (meme/guide/articles/translations/infographics/videos, at iba pa)
Tier 5 - 10 Ibinibigay batay sa iyong aktibidad sa proyekto
Maaari ka rin mag-generate ng larawan sa https://bc8.ai/ at ipadala ang iyong resulta sa Discord #made-witc-bc8."""

    roles_info_korean = """ 서버에는 총 10개의 티어 역할 및 모더레이터 또는 기술 지원 역할이 있습니다.

티어 1 - 이 역할을 받으려면 디스코드 서버에서 인증하고 #wallet-submission 분기에 소라나 지갑을 연결해야 합니다.
티어 2 - 이 역할을 받으려면 AMA 이벤트에 참여해야 합니다(매주 수요일 - Discord/이벤트에서 시간 확인) 또는 디스코드의 다양한 분기에서 모더레이터의 추첨에 참여해야 합니다.
티어 3+ (팀에서만 발급) - 이 역할을 받으려면 Discord에서 최대한 활동적이고 유용한 사람이어야 합니다.
티어 4 (대사) - 이 역할을 받으려면 새로 온 사람들을 돕고, 그들의 트위터와 상호 작용하며 품질 높은 콘텐츠(미미/가이드/기사/번역/인포그래픽/동영상 등)를 만들어야 합니다.
티어 5 - 10은 프로젝트 내 활동에 따라 부여됩니다.
또한 https://bc8.ai/에서 이미지를 생성하고 Discord #made-witc-bc8에 결과를 보낼 수 있습니다. """

    roles_info_china = """ 在服务器上总共有10个级别角色 + 管理员或技术支持角色

一级 - 要获得此角色，您需要在Discord服务器上进行验证，并在 #wallet-submission 分支中连接您的 SOLANA 钱包
二级 - 要获得此角色，您需要参加AMA活动（每周三 - 请查看Discord/活动中的时间），或者在Discord的不同分支中参加管理员的抽奖
三级+（仅由团队分发）- 要获得此角色，您需要在Discord中尽可能活跃/有用
四级（大使）- 要获得此角色，您需要帮助新手/与他们的Twitter互动/创建高质量内容（模因/指南/文章/翻译/信息图/视频等）
五级 - 十级根据您在项目中的活动而授予
您还可以在 https://bc8.ai/ 生成图像，并将结果发送到 Discord 的 #made-witc-bc8。"""

    roles_info_portugal = """ No servidor, existem no total 10 - Papéis de Nível + Papéis de Moderador ou Assistente Técnico

Nível 1 - Para obter este papel, você precisa se verificar no servidor do Discord e conectar sua carteira SOLANA no canal #wallet-submission
Nível 2 - Para obter este papel, você precisa participar dos eventos AMA (todas as quartas-feiras - verifique o horário no Discord/Eventos) ou sorteios dos moderadores em diferentes canais do Discord
Nível 3+ (Concedido exclusivamente pela equipe) - Para obter este papel, você precisa ser o mais ativo / útil possível no Discord
Nível 4 (Embaixador) - Para obter este papel, você precisa ajudar os novatos / interagir com o Twitter deles / criar conteúdo de qualidade (memes/guias/artigos/traduções/infográficos/vídeos e assim por diante)
Nível 5 - 10 É concedido com base em sua atividade no projeto
Você também pode gerar uma imagem em https://bc8.ai/ e enviar seu resultado para o Discord #made-witc-bc8."""

    roles_info_turkish = """ Sunucuda toplamda 10 - Kademe Rolleri ve Moderatör veya Teknik Destek Rolleri bulunmaktadır

Kademe 1 - Bu rolü almak için Discord sunucusunda doğrulama yapmanız ve SOLANA cüzdanınızı #wallet-submission kanalına bağlamanız gerekmektedir.
Kademe 2 - Bu rolü almak için AMA etkinliklerine katılmanız gerekmektedir (Her Çarşamba - Saati Discord/Olaylar bölümünden kontrol edin) veya Discord'un farklı kanallarında moderatörlerin çekilişlerine katılmanız gerekmektedir.
Kademe 3+ (Yalnızca takım tarafından verilir) - Bu rolü almak için Discord'da maksimum derecede aktif / yararlı olmanız gerekmektedir.
Kademe 4 (Elçi) - Bu rolü almak için yeni başlayanlara yardımcı olmanız / onların Twitter ile etkileşimde bulunmanız / kaliteli içerik oluşturmanız gerekmektedir (meme/rehber/makale/çeviri/infografik/video ve daha fazlası)
Kademe 5 - 10, projedeki etkinliğinize bağlı olarak verilir.
Ayrıca https://bc8.ai/ adresinde bir resim oluşturabilir ve sonucunuzu Discord #made-witc-bc8 kanalına gönderebilirsiniz."""

    roles_info_poland = """ Na serwerze istnieje łącznie 10 - Role Tier + Role Moderatora lub Asystenta Technicznego

Poziom 1 - Aby uzyskać tę rolę, musisz zweryfikować się na serwerze Discord i podłączyć swój portfel SOLANA do gałęzi #wallet-submission
Poziom 2 - Aby uzyskać tę rolę, musisz brać udział w wydarzeniach AMA (każdą środę - sprawdź godzinę na Discord/Ogłoszenia) lub w losowaniach moderatorów na różnych kanałach Discorda
Poziom 3+ (Wydawany wyłącznie przez zespół) - Aby uzyskać tę rolę, musisz być maksymalnie aktywną / pomocną osobą na Discordzie
Poziom 4 (Ambasador) - Aby uzyskać tę rolę, musisz pomagać nowym użytkownikom / współpracować z ich kontami Twitter / tworzyć wysokiej jakości treści (memy/przewodniki/artykuły/tłumaczenia/infografiki/filmy itp.)
Poziom 5 - 10 Przyznawany jest w zależności od Twojej aktywności w projekcie
Możesz również wygenerować obraz na https://bc8.ai/ i wysłać swój wynik na Discordzie do #made-witc-bc8."""

    roles_info_italian = """ Nel server ci sono in totale 10 - Ruoli Tier + Ruoli di Moderatore o Assistente Tecnico

Livello 1 - Per ottenere questo ruolo, devi verificarti sul server Discord e collegare il tuo portafoglio SOLANA nel canale #wallet-submission
Livello 2 - Per ottenere questo ruolo, devi partecipare agli eventi AMA (ogni mercoledì - controlla l'orario su Discord/Eventi) o partecipare alle estrazioni dei moderatori in diversi canali Discord
Livello 3+ (Assegnato esclusivamente dal team) - Per ottenere questo ruolo, devi essere il più attivo / utile possibile su Discord
Livello 4 (Ambasciatore) - Per ottenere questo ruolo, devi aiutare i nuovi arrivati / interagire con il loro Twitter / creare contenuti di qualità (meme/guide/articoli/traduzioni/infografiche/video, ecc.)
Livello 5 - 10 Viene assegnato in base alla tua attività nel progetto
Puoi anche generare un'immagine su https://bc8.ai/ e inviare il tuo risultato su Discord a #made-witc-bc8."""

    roles_info_romanian = """ Pe server există în total 10 - Roluri Tier + Roluri de Moderator sau Asistent Tehnic

Nivelul 1 - Pentru a obține acest rol, trebuie să vă verificați pe serverul Discord și să conectați portofelul SOLANA în canalul #wallet-submission
Nivelul 2 - Pentru a obține acest rol, trebuie să participați la evenimentele AMA (în fiecare miercuri - verificați ora pe Discord/Evenimente) sau la extragerile moderatorilor în diferite canale Discord
Nivelul 3+ (Acordat exclusiv de echipă) - Pentru a obține acest rol, trebuie să fiți cât mai activ / util posibil pe Discord
Nivelul 4 (Ambasador) - Pentru a obține acest rol, trebuie să ajutați începătorii / să interacționați cu conturile lor de Twitter / să creați conținut de calitate (memes/ghiduri/articole/traduceri/infografice/videoclipuri etc.)
Nivelul 5 - 10 Este acordat în funcție de activitatea dvs. în proiect
De asemenea, puteți genera o imagine pe https://bc8.ai/ și să trimiteți rezultatul în Discord la #made-witc-bc8. """

    roles_info_dutch = """ "Op de server zijn in totaal 10 - Tier Rollen + Rollen van Moderator of Technische Assistent:
1) Tier 1 - om deze rol te verkrijgen, moet u zich verifiëren op de Discord-server en uw SOLANA-portemonnee aansluiten op de #wallet-submission tak
2) Tier 2 - om deze rol te verkrijgen, moet u deelnemen aan AMA-evenementen (elke woensdag - controleer de tijd in Discord / Evenementen) of aan loterijen georganiseerd door moderators in verschillende Discord-takken
3) Tier 3+ (Wordt exclusief toegekend door het team) - om deze rol te verkrijgen, moet u een zeer actief / nuttig persoon zijn in Discord
4) Tier 4 (Ambassadeur) - om deze rol te verkrijgen, moet u nieuwkomers helpen / communiceren met hun Twitter / hoogwaardige inhoud maken (memes / gidsen / artikelen / vertalingen / infographics / video's enzovoort)
5) Tier 5 - 10 Wordt toegekend op basis van uw activiteit in het project
U kunt ook een afbeelding genereren op https://bc8.ai/ en uw resultaat verzenden in Discord #made-witc-bc8 """

    roles_info_english = """On the server, there are 10 levels of roles + Moderator or Technical Assistant roles:
1) Level 1 - To obtain this role, you need to undergo verification on the Discord server and connect your SOLANA wallet to the #wallet-submission branch.
2) Level 2 - To obtain this role, you need to participate in AMA events (Every Wednesday - check the time in Discord/Events) or participate in giveaways from moderators in various Discord channels.
3) Level 3+ (awarded exclusively by the command) - To obtain this role, you need to be maximally active and helpful participant on the Discord server.
4) Level 4 (Ambassador) - To obtain this role, you need to help newcomers, interact with their Twitter, create quality content (memes, guides, articles, translations, infographics, videos, etc.).
5) Levels 5-10 - Awarded based on your activity in the project.

You can also create an image at https://bc8.ai/ and submit your result to Discord #made-witc-bc8."""

    selected_language = chat_states.get(message.chat.id, "Russia")
    if selected_language == "Russia":
        bot.send_message(message.chat.id, roles_info_russian)
    elif selected_language == "Ukraine":
        bot.send_message(message.chat.id, roles_info_ukrainian)
    elif selected_language == "French":
        bot.send_message(message.chat.id, roles_info_french)
    elif selected_language == "German":
        bot.send_message(message.chat.id, roles_info_german)
    elif selected_language == "Spanish":
        bot.send_message(message.chat.id, roles_info_spanish)
    elif selected_language == "Indonesian":
        bot.send_message(message.chat.id, roles_info_indonesian)
    elif selected_language == "Malay":
        bot.send_message(message.chat.id, roles_info_malay)
    elif selected_language == "Vietnamese":
        bot.send_message(message.chat.id, roles_info_vietnamese)
    elif selected_language == "Japan":
        bot.send_message(message.chat.id, roles_info_japan)
    elif selected_language == "Hindi":
        bot.send_message(message.chat.id, roles_info_hindi)
    elif selected_language == "Filipino":
        bot.send_message(message.chat.id, roles_info_filipino)
    elif selected_language == "Korean":
        bot.send_message(message.chat.id, roles_info_korean)
    elif selected_language == "China":
        bot.send_message(message.chat.id, roles_info_china)
    elif selected_language == "Portugal":
        bot.send_message(message.chat.id, roles_info_portugal)
    elif selected_language == "Turkish":
        bot.send_message(message.chat.id, roles_info_turkish)
    elif selected_language == "Poland":
        bot.send_message(message.chat.id, roles_info_poland)
    elif selected_language == "Italian":
        bot.send_message(message.chat.id, roles_info_italian)
    elif selected_language == "Romanian":
        bot.send_message(message.chat.id, roles_info_romanian)
    elif selected_language == "Dutch":
        bot.send_message(message.chat.id, roles_info_dutch)
    elif selected_language == "English":
        bot.send_message(message.chat.id, roles_info_english)


def send_galxe_link(message):
    chat_id = message.chat.id
    selected_language = chat_states.get(chat_id, "Russia")
    galxe_link = galxe_links.get(selected_language, "https://galxe.com/io.net")

    message_texts = {
        "Russia": 'Ссылка на Galxe:',
        "Ukraine": 'Посилання на Galxe:',
        "French": 'Lien vers Galxe:',
        "German": "Link zu Galxe",
        "Arabic": "رابط Galxe",
        "Spanish": "Enlace a Galxe",
        "Indonesian": "Link ke Galxe",
        "Malay": "Link ke Galxe",
        "Vietnamese": "Liên kết đến Galxe",
        "Japan": "Galxeへのリンク",
        "Hindi": "Galxe के लिए लिंक",
        "Filipino": "Link sa Galxe",
        "Korean": "Galxe 링크",
        "China": "链接到 Galxe",
        "Portugal": "Link para Galxe",
        "Turkish": "Galxe'ye bağlantı",
        "Poland": "Odnośnik do Galxe",
        "Italian": "Collegamento a Galxe",
        "Romanian": "Link către Galxe",
        "Dutch": "Link naar Galxe",
    }

    message_text = message_texts.get(selected_language, 'Link to Galxe:')

    print("Received message:", message.text)  # Добавьте эту строку для отслеживания текста сообщения
    chat_id = message.chat.id

    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(message_text, url=galxe_link))
    bot.send_message(chat_id, message_text, reply_markup=markup)


def translate_buttons(buttons, language):
    translations = {
        "English": ["Mac", "Windows", "Linux", "Explanation of Work Status", "Back"],
        "Russia": ["Mac", "Windows", "Linux", "Обьяснение Статуса Работника", "Назад"],
        "Ukraine": ["Mac", "Windows", "Linux", "Роз'яснення статусу працівника", "Назад"],
        "French": ["Mac", "Windows", "Linux", "Explication du statut de l’employé", "Retour"],
        "German": ["Mac", "Windows", "Linux", "Erläuterung des Status des Mitarbeiters", "Zurück"],
        "Spanish": ["Mac", "Windows", "Linux", "Explicación de la situación del empleado", "Volver"],
        "Indonesian": ["Mac", "Windows", "Linux", "Penjelasan status karyawan", "Kembali"],
        "Malay": ["Mac", "Windows", "Linux", "Kesilapan Yang Mungkin", "Kembali"],
        "Vietnamese": ["Mac", "Windows", "Linux", "Giải thích về tình trạng của nhân viên", "Quay lại"],
        "Japan": ["Mac", "Windows", "Linux", "従業員のステータスの説明", "バック"],
        "Hindi": ["Mac", "Windows", "Linux", "कर्मचारी की स्थिति का स्पष्टीकरणं", "पीछे जाएं"],
        "Filipino": ["Mac", "Windows", "Linux", "Paliwanag sa katayuan ng empleyado", "Bumalik"],
        "Korean": ["Mac", "Windows", "Linux", "직원의 상태에 대한 설명", "뒤로가기"],
        "China": ["Mac", "Windows", "Linux", "對員工身份的解釋", "返回"],
        "Portugal": ["Mac", "Windows", "Linux", "Explicação do estatuto do trabalhador", "Voltar"],
        "Turkish": ["Mac", "Windows", "Linux", "Çalışanın durumunun açıklanması", "Geri"],
        "Poland": ["Mac", "Windows", "Linux", "Wyjaśnienie statusu pracownika", "Wstecz"],
        "Italian": ["Mac", "Windows", "Linux", "Spiegazione dello status del dipendente", "Indietro"],
        "Romanian": ["Mac", "Windows", "Linux", "Explicarea statutului angajatului", "Înapoi"],
        "Dutch": ["Mac", "Windows", "Linux", "Uitleg over het statuut van de werknemer", "Terug"],
        # Добавьте переводы для других языков
    }

    return translations.get(language, buttons)


def send_nodes_menu(message):
    chat_id = message.chat.id
    selected_language = chat_states.get(chat_id, "Russia")

    nodes_menu_buttons = translate_buttons(["Mac", "Windows", "Linux", "Explanation of Work Status", "Back"],
                                           selected_language)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*nodes_menu_buttons)

    nodes_menu_messages = {
        "English": "Choose Your Operating System:",
        "Russia": "Выберите вашу операционную систему:",
        "Ukraine": "Виберіть вашу операційну систему:",
        "French": "Choisissez votre système d’exploitation:",
        "German": "Wählen Sie Ihr Betriebssystem:",
        "Spanish": "Elige tu sistema operativo:",
        "Indonesian": "Pilih Sistem Operasi Anda:",
        "Malay": "Pilih Sistem Pengendalian Anda:",
        "Vietnamese": "Chọn hệ điều hành của bạn:",
        "Japan": "オペレーティング システムの選択:",
        "Hindi": "अपना ऑपरेटिंग सिस्टम चुनें:",
        "Filipino": "Piliin ang Iyong Operating System:",
        "Korean": "운영 체제 선택:",
        "China": "選擇您的作業系統:",
        "Portugal": "Escolha seu sistema operacional:",
        "Turkish": "İşletim Sisteminizi Seçin:",
        "Poland": "Wybierz swój system operacyjny:",
        "Italian": "Scegli il tuo sistema operativo:",
        "Romanian": "Alegeți sistemul de operare:",
        "Dutch": "Kies uw besturingssysteem:",
        # Добавьте остальные языки
    }

    nodes_menu_message = nodes_menu_messages.get(selected_language, "Choose your operating system:")

    bot.send_message(chat_id, nodes_menu_message, reply_markup=markup)


bot.polling(none_stop=True)
