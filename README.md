# 逃走中 THE MOVIE「Escape from SAZAE」

## 概要
このゲームは、カツオ（プレイヤー）が宿題をやらずに遊びに行こうとする場面で、サザエ（ハンター）から逃げ切ることを目指す追跡ゲームです。
プレイヤーは、サザエの追撃を振り切り、中島の待つ公園で野球をすることを目標に進行します。

---

## ゲームのルール

### 初期設定
- **カツオの初期位置**: 3
- **サザエの初期位置**: 0
- **ゴール**: カツオが位置10に到達すると勝利
- **ハンターの初期速度**: サザエは通常1マスずつ進行

### 勝敗条件
- **勝利条件**:
  - カツオが10マス目に到達する。
- **敗北条件**:
  - サザエに追いつかれる。

### 基本操作
1. 毎ターン、カツオの進む方向を選択する。
   - 選択肢：北、南、東、西
2. 毎ターン、イベントがランダムに発生。
3. イベントやアイテムを活用してサザエの動きを遅らせながら逃げる。

---

## ゲームのイベント

### イベント一覧
1. **どらねこ**
   - 魚をくわえたどらねこを捕まえると、アイテム「どらねこ」が手に入る。
   - 効果: サザエの動きを1マス遅らせる。

2. **じゃんけん**
   - サザエとじゃんけん対決。
     - 勝利: サザエの動きを1ターン止める。
     - 敗北: サザエの速度が2にアップ。
     - あいこ: 何も起きない。

3. **友人の協力**
   - カツオの同級生が登場し、友情効果が発動。
   - 効果: サザエと友人が遭遇すると、サザエの動きを2マス遅らせる。

4. **井戸端会議**
   - サザエがたいこさんまたはノリスケさんと立ち話。
   - 効果: サザエの動きを1マス遅らせる。

5. **花澤さん**
   - 花澤さんがカツオに話しかけてきて、足止めされる。
   - 効果: サザエが1マス近づく。

---

## ゲームの進行

### 1. スタート
ゲーム開始時、カツオが中島と野球をするために逃げることを宣言。サザエが追いかけてきます。

### 2. 毎ターンの流れ
1. カツオが移動する方向を選択（北、南、東、西）。
2. イベントがランダムで発生。
3. イベントの結果に応じて、カツオまたはサザエの位置や速度が変化。
4. サザエがカツオを追いかけて1マス（または速度に応じた距離）進む。
5. 勝敗条件をチェック。

### 3. 終了条件
- カツオがゴール（位置10）に到達すると「勝利」
- サザエがカツオに追いつくと「敗北」

---

## 実行例

### スタート時
```
カツオー！！また宿題やらずに遊びに行こうとして！今日という今日は逃がさないんだからね！！
今日は中島と野球をする約束なんだ！絶対逃げてやる！
逃走中START！ハンター：サザエから逃げ切ってください！
```

### イベント発生例
#### **どらねこ**
```
イベントが発生しました！
魚をくわえたどらねこが現れた！何かに使えるかもしれない。捕まえよう！
1. そっと近づいて捕まえる
2. 素早く近づいて捕まえる
選択肢を入力してください (1-2): 1
どらねこを捕まえた！アイテム欄にどらねこが追加されました！
```

#### **じゃんけん**
```
イベントが発生しました！
サザエ：こほん...さーて、来週のサザエさんは？
...じゃん、けん...
何を出す？
1: グー
2: チョキ
3: パー
選択肢を入力してください (1-3): 3
ぽん！！
カツオ: パー, サザエ: チョキ
じゃんけんに勝った！サザエの動きを1ターン止めることに成功！
```

### 結果
#### **勝利**
```
はあ、はあ、中島！遅れてごめん！
中島：待ちくたびれたよ！さあ、野球やろう！
無事に野球を満喫できた！
ゲームクリア！！
```

#### **敗北**
```
サザエ：ふん！捕まえたわよカツオ！！家に帰って宿題しなさい！！
カツオ：そ、そんなぁ...
カツオ 確保
ゲームオーバー...
```
