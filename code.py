'''
課題３ その他 自由なテーマのプログラムを作成
自由なテーマでプログラムを作成してください。 ただし、以下の条件を満たすこと。

- 何を目的としたプログラムかを説明すること
- その目的を達成するために、どのような機能を持つプログラムかを説明すること
- そのプログラムを実行すると、どのような結果が得られるかを説明すること
- 講義で学んだ内容をできるだけ多く盛り込むこと
- 複数の関数を定義し、それらの関数を呼び出すこと
- 講義で扱っていない内容を取り入れても構いません。
'''


'''
逃走中 THE MOVIE「Escape from SAZAE」

<概要>
カツオとなり、宿題をしないで遊びに行こうとするところを追いかけてくるサザエから逃げ切るゲーム。サザエ（ハンター）を振り切り、野球友達の中島の待つ公園を目指す。


<ルール>
・初期設定
    カツオ（プレイヤー）は初期位置3、サザエ（ハンター）は初期位置0からスタート。
    目標位置は10。サザエに捕まらずに10マス先に到達すると勝利。

・移動
    カツオは毎ターン東西南北に移動できます（実際には位置は常に1マス進む）。
    サザエは基本速度1で追いかけてくるが、特定条件を満たすと速度が変わることがある。

・イベント
    ゲーム中にイベントがランダムに発生する。プレイヤーの選択次第で状況が有利になったり、不利になったりする。
    【イベント一覧】
    ・どらねこ
        「魚をくわえたどらねこ」が出現。捕まえれば「サザエの動きを1マス遅らせるアイテム」として手に入ります。
    ・じゃんけん:
        サザエとじゃんけん対決をする。勝てばサザエの動きを1ターン止められるが、負けるとサザエの速度が2にアップする。
    ・友人の協力
        カツオの同級生が現れ、カツオの頼み方次第で友情効果が発動する。その同級生がサザエと遭遇すると2マス遅らせてくれる。
    ・井戸端会議
        サザエがたいこさんまたはノリスケさんと立ち話を始め、サザエの動きを1マス遅らせる。
    ・花澤さん
        花澤さんに遭遇し、会話に巻き込まれる。サザエが1マス近づく。

・勝敗条件
  - 勝利：カツオが10マス目に到達すると、無事にサザエを振り切り、中島と野球を楽しめる。
  - 敗北：サザエに追いつかれるとカツオは捕まり、宿題をやらさる。

'''


# ほぼチャットGPTで作ったゲームです。

import random
import time

def display_message(message):
    """メッセージを表示し、少し待機"""
    print(message)
    time.sleep(1.5)

def display_status(player_position, hunter_position, ally_active, hunter_speed):
    """プレイヤーとハンターの状態を表示"""
    print("\n=== 状態 ===")
    print(f"カツオの位置: {player_position}")
    print(f"サザエの位置: {hunter_position}")
    print(f"サザエの速度: {hunter_speed}")
    if ally_active:
        print("友情効果: 発動中！サザエと友人が遭遇すると2マス遅らせる")
    else:
        print("友情効果: なし")
    print("===================")

def move_player():
    """プレイヤーが移動する方向を選ぶ"""
    directions = ["北", "南", "東", "西"]
    print("どの方向に逃げますか？")
    for i, direction in enumerate(directions):
        print(f"{i + 1}: {direction}")
    while True:
        try:
            choice = int(input("選択肢を入力してください (1-4): "))
            if 1 <= choice <= 4:
                return directions[choice - 1]
            else:
                print("1から4の数字を入力してください。")
        except ValueError:
            print("無効な入力です。数字を入力してください。")

def use_item(items, player_position, hunter_position):
    """アイテムを使用するか選択"""
    if not items:
        print("アイテム欄は空です。")
        return None, player_position, hunter_position
    print("\nアイテム欄:")
    for i, item in enumerate(items):
        print(f"{i + 1}: {item['名前']} - {item['説明']}")
    print("0: アイテムを使わない")
    while True:
        try:
            choice = int(input("使うアイテムを選んでください (0-{}): ".format(len(items))))
            if 0 <= choice <= len(items):
                if choice == 0:
                    return None, player_position, hunter_position
                item = items.pop(choice - 1)
                if item["名前"] == "どらねこ":
                    hunter_position -= 1  # ハンターを1マス後退させる
                    display_message("どらねこを使ってサザエの動きを1マス遅らせた！")
                return item, player_position, hunter_position
            else:
                print(f"0から{len(items)}の数字を入力してください。")
        except ValueError:
            print("無効な入力です。数字を入力してください。")

def janken_event(hunter_speed):
    """じゃんけんイベント"""
    display_message("サザエ：大変！もうこんな時間！")
    display_message("サザエ：こほん...さーて、来週のサザエさんは？")
    display_message("...")
    display_message("サザエ：来週もまたみてくださいね！じゃん、けん...")
    print("何を出す？")

    # ハンターの手をランダムに決定（勝つ確率を75%に調整）
    hunter_hand = random.choices(["グー", "チョキ", "パー"], weights=[25, 25, 50], k=1)[0]
    print("ぽん！！")

    # プレイヤーの手を選択
    print("どの手を出しますか？")
    print("1: グー")
    print("2: チョキ")
    print("3: パー")
    while True:
        try:
            player_choice = int(input("選択肢を入力してください (1-3): "))
            if player_choice == 1:
                player_hand = "グー"
            elif player_choice == 2:
                player_hand = "チョキ"
            elif player_choice == 3:
                player_hand = "パー"
            else:
                print("1から3の数字を入力してください。")
                continue
            break
        except ValueError:
            print("無効な入力です。数字を入力してください。")

    print(f"カツオ: {player_hand}, サザエ: {hunter_hand}")

    # 勝敗判定
    if (player_hand == "グー" and hunter_hand == "チョキ") or \
       (player_hand == "チョキ" and hunter_hand == "パー") or \
       (player_hand == "パー" and hunter_hand == "グー"):
        display_message("ふふふふふふふ...")
        display_message("じゃんけんに勝った！サザエの動きを1ターン止めることに成功！")
        return hunter_speed, True  # 速度は変えずに、進行を1ターン止める
    elif player_hand == hunter_hand:
        display_message("ふふふふふふふ")
        display_message("あいこだった。何も起きない。")
        return hunter_speed, False  # 速度は変わらず、何も起きない
    else:
        display_message("ふふふふふふふ！！")
        display_message("じゃんけんに負けた…サザエの進行が2になる")
        return 2, False  # ハンターの速度を2にする

def encounter_event(items, hunter_position, ally_active, event_flags, hunter_speed):
    """ランダムなイベントを発生させ、プレイヤーの選択によって異なる効果を適用"""
    print("\nイベントが発生しました！")
    
    # イベントの発生確率を設定
    events = ["どらねこ", "花澤", "井戸端"]
    weights = [20, 20, 30]  # どらねこ:20%、花澤:10%、井戸端:45%
    
    # 「友人」イベントは一度だけ発生可能
    if not event_flags["友人発生済み"]:
        events.append("友人")
        weights.append(20)  # 友人:15%

    # 「じゃんけん」イベントは一度だけ発生可能
    if not event_flags["じゃんけん発生済み"]:
        events.append("じゃんけん")
        weights.append(10)  # じゃんけん:10%

    event = random.choices(events, weights=weights, k=1)[0]
    
    if event == "じゃんけん":
        event_flags["じゃんけん発生済み"] = True
        hunter_speed, stop_hunter = janken_event(hunter_speed)
        return 0, hunter_position, ally_active, event_flags, hunter_speed, stop_hunter

    if event == "どらねこ":
        print("魚をくわえたどらねこが現れた！何かに使えるかもしれない。捕まえよう！")
        print("1. そっと近づいて捕まえる")
        print("2. 素早く近づいて捕まえる")
        correct_box = random.choice(["1", "2"])  # 正解の方法をランダムに決定
        choice = input("選択肢を入力してください (1-2): ")
        if choice == correct_box:
            display_message("どらねこを捕まえた！アイテム欄にどらねこが追加されました！")
            items.append({"名前": "どらねこ", "説明": "サザエの気をどらねこに引き付けることができる。サザエの動きを1マス遅らせる。"})
            return 0, hunter_position, ally_active, event_flags, hunter_speed, False
        else:
            display_message("逃げられた...")
            return 0, hunter_position, ally_active, event_flags, hunter_speed, False

    if event == "友人":
        event_flags["友人発生済み"] = True  # 友人イベント発生済みに設定
        display_message("同級生：カツオ！そんなに急いでどうしたんだ？")
        display_message("カツオ：今姉さんに追われているんだ！見かけたら足止めしてくれないか？")
        display_message("同級生：うーん...どうしようかな～")
        display_message("カツオ：いまいち協力してくれそうにない...かくなる上は...！！")
        print("どうやってお願いする？")
        print("1. 次の掃除当番を変わる")
        print("2. 土下座")
        print("3. うるさいさっさとやれ")
        choice = input("選択肢を入力してください (1-3): ")
        
        if choice == "1":
            display_message("同級生：え！やったぁ！！カツオ任せとけ！ばっちり守ってやるよ")
            display_message("友情効果発動！同級生がサザエと出会った際にサザエの動きを2マス遅らせることができる")
            return 0, hunter_position, True, event_flags, hunter_speed, False  # 友情効果を有効化
        elif choice == "2":
            display_message("同級生：うーん、気持ちは伝わったけど…何もできそうにないなぁ。")
            return 0, hunter_position, ally_active, event_flags, hunter_speed, False
        elif choice == "3":
            display_message("同級生：は？なんだよお前。サザエさーん！！カツオはここですよーーー！！！！")
            display_message("まずい...！！さすがにものを頼む立場として失礼すぎたか...")
            return 0, hunter_position, ally_active, event_flags, hunter_speed, False

    if event == "花澤":
        display_message("花澤：あれ？カツオ君じゃない！")
        display_message("カツオ：は、花澤さん！？どうしてここに...")
        display_message("花澤：さっきサザエさんの大きい声が聞こえたからね。それよりこの後時間ある？どっか一緒に行かない？")
        display_message("花澤：それよりこの後時間ある？どっか一緒に行かない？")
        display_message("カツオ：い、いや～僕はちょっと遠慮しておこうかな～あはは...")
        display_message("花澤：つれないわねぇ、ちょっとぐらいいでしょ？")
        display_message("---------------------")
        print("花澤を振り切るのに時間がかかった！サザエが1マス近づく")
        return 1, hunter_position, ally_active, event_flags, hunter_speed, False
    
    if event == "井戸端":
        person = random.choice(["たいこ", "ノリスケ"])
        
        if person == "たいこ":
            display_message("たいこ：サザエさん？こんなところでどうしたんですか？")
            display_message("サザエ：あら、たいこさん！ちょっと聞いてよ～さっきうちのカツオがね...")
            display_message("カツオ：（よし！チャンスだ！井戸端会議をしている間に逃げよう！）")
            print("---------------")
            print("サザエの動きを1マス遅らせた！")
        elif person == "ノリスケ":
            display_message("ノリスケ：あれ？サザエさんじゃないですか！")
            display_message("サザエ：あっノリスケさん！")
            display_message("ノリスケ：いや～偶然ですね！そういえば聞いてくださいよ！この間おじさんと飯に行ったんですけど...")
            display_message("サザエ：あ...へーそうなんですね～...")
            display_message("カツオ：（よし！チャンスだ！姉さんがノリスケさんに押されてる間に逃げよう！）")
            print("---------------")
            print("サザエの動きを1マス遅らせた！")

        # ハンターの動きを1マス遅らせる
        return 0, hunter_position - 1, ally_active, event_flags, hunter_speed, False


def game():
    """逃走中ゲームのメイン関数"""
    display_message("逃走中 THE MOVIE「Escape from SAZAE」")
    display_message("カツオー！！また宿題やらずに遊びに行こうとして！今日という今日は逃がさないんだからね！！")
    display_message("今日は中島と野球をする約束なんだ！絶対逃げてやる！")
    display_message("逃走中START！ハンター：サザエから逃げ切ってください！")
    display_message("キャラクターの解釈違いがあったらすみません")
    print("--------------------------------")
    player_position = 3  # プレイヤーの初期位置を3に設定
    hunter_position = 0
    goal = 10
    items = []  # プレイヤーのアイテム欄
    ally_active = False  # 友情効果のステータス
    hunter_speed = 1  # ハンターの初期速度
    event_flags = {"友人発生済み": False, "じゃんけん発生済み": False}  # イベントの発生状況を管理

    while True:
        display_status(player_position, hunter_position, ally_active, hunter_speed)
        
        # アイテムの使用
        item, player_position, hunter_position = use_item(items, player_position, hunter_position)
        
        direction = move_player()
        display_message(f"{direction}に向かって逃げた！")
        
        # プレイヤーの進行とイベント処理
        player_position += 1
        event_effect, hunter_position, ally_active, event_flags, hunter_speed, stop_hunter = encounter_event(
            items, hunter_position, ally_active, event_flags, hunter_speed)
        
        # ハンターの進行を止める場合
        if stop_hunter:
            display_message("サザエは動けない！")

        # ハンターの進行
        else:
            hunter_position += hunter_speed
        
        # ゲームオーバー判定
        if player_position <= hunter_position:
            display_message("サザエ：ふん！捕まえたわよカツオ！！家に帰って宿題しなさい！！")
            display_message("カツオ：そ、そんなぁ...")
            display_message("カツオ 確保")
            display_message("ゲームオーバー...")
            break
        
        # 勝利条件判定
        if player_position >= goal:
            display_message("-----公園------")
            display_message("カツオ：はあ、はあ、中島！遅れてごめん！")
            display_message("中島：待ちくたびれたよ！さあ、野球やろう！")
            display_message("無事に野球を満喫できた！")
            display_message("ゲームクリア！！")
            break

if __name__ == "__main__":
    game()

