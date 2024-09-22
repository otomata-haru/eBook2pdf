
# 電子書籍スキャナー 使用説明書

## 概要

**電子書籍スキャナー**は、指定した範囲のスクリーンショットを自動的に取得し、それらを1つのPDFファイルにまとめるソフトウェアです。電子書籍やウェブページなどのページを自動でめくりながらキャプチャし、PDFとして保存できます。

---

## 特徴

- **簡単操作**：直感的なGUIで操作が簡単。
- **自動ページめくり**：指定したキーやクリックでページを自動的にめくります。
- **領域指定**：キャプチャしたい画面領域を自由に指定できます。
- **PDF出力**：取得した画像をPDFファイルとして保存します。
- **終了通知**：処理終了後にチャイム音でお知らせします（オプション）。

---

## 動作環境

- **対応OS**：Windows 10 / Windows 11
- **必要ライブラリ**：特別なライブラリは不要です。インストーラーに含まれています。

---

## インストール方法

1. **ダウンロード**

   - 提供された`ebook2pdf.exe`ファイルをダウンロードします。

2. **実行**

   - ダウンロードした`ebook2pdf.exe`をダブルクリックして起動します。
   - インストールは不要です。そのまま実行できます。

---

## 使い方

### 1. プログラムの起動

- `ebook2pdf.exe`をダブルクリックしてプログラムを起動します。

### 2. 本のタイトルを入力

- メイン画面上部の「**本のタイトル**」欄に、保存したいPDFファイルの名前を入力します。
  - 例：`サンプル電子書籍`

### 3. ページめくりの設定

- 「**ページめくり**」オプションから、ページをめくる方法を選択します。

  - **←キー**：左矢印キーでページをめくります。
  - **→キー**：右矢印キーでページをめくります。
  - **スペースキー**：スペースキーでページをめくります。
  - **左クリック**：マウスの左クリックでページをめくります。

### 4. 取得間隔時間の設定

- 「**取得間隔時間**」に、各ページのスクリーンショットを取得する間隔（秒）を入力します。
  - 例：`1`（1秒ごとにスクリーンショットを取得）

### 5. 終了後のチャイム設定（任意）

- 「**終了後チャイムを鳴らす**」にチェックを入れると、処理完了後にチャイム音が鳴ります。

### 6. キャプチャ範囲の指定

- 「**実行**」ボタンをクリックすると、画面全体が暗くなり、キャプチャしたい範囲を指定できます。

  1. **範囲選択**：マウスでキャプチャしたい領域をドラッグして選択します。
  2. **確定**：マウスボタンを離すと、選択が確定します。

### 7. スクリーンショットの開始

- キャプチャ範囲を指定すると、自動的にスクリーンショットの取得が開始されます。

  - **重要**：
    - **電子書籍を表示しているウィンドウがアクティブでないと、スクリーンショットの取得が始まりません**。キャプチャを開始する前に、電子書籍のウィンドウをアクティブにしてください。
    - **スクリーンショット中はPCを操作しないでください**。このソフトウェアはスクリーンショットを使用してページを保存するため、他の操作を行うとキャプチャが正しく行われない可能性があります。

### 8. 処理の完了

- スクリーンショットの取得が完了すると、指定したタイトル名でPDFファイルが作成されます。
- 「**保存完了！**」と画面に表示されます。
- チャイム設定をオンにしている場合、音が鳴ります。

---

## 注意事項

- **電子書籍ウィンドウのアクティブ化**：スクリーンショットの取得は、電子書籍を表示しているウィンドウがアクティブな状態でなければ開始されません。キャプチャ範囲の指定後、必ず電子書籍のウィンドウを最前面に表示してください。

- **PCの操作制限**：スクリーンショット取得中は、他の操作（マウスやキーボードの入力、ウィンドウの切り替えなど）を行わないでください。操作を行うと、正しくスクリーンショットが取得できない場合があります。

- **著作権に関する注意**：電子書籍やウェブページのスクリーンショットを取得する際は、**著作権法を遵守**してください。個人利用の範囲を超える利用は法律で禁止されています。

- **動作環境**：このソフトウェアは**Windows専用**です。他のOSでは動作しません。

- **スクリーンセーバーや電源設定**：長時間の処理を行う場合、**スクリーンセーバーや自動スリープを無効**にしてください。

---

## トラブルシューティング

### Q1. スクリーンショットがうまく取得できない

- **対処法**：
  - **電子書籍のウィンドウがアクティブになっているか確認**してください。他のウィンドウが前面にあると、キャプチャが開始されません。
  - スクリーンショットを取得したいウィンドウが最前面に表示されているか確認してください。
  - 他のウィンドウや通知が被らないようにしてください。

### Q2. PDFファイルが生成されない

- **対処法**：
  - 保存先に十分な空き容量があるか確認してください。
  - スクリーンショット中にPCを操作していなかったか確認してください。
  - プログラムを再起動して、もう一度試してください。

### Q3. プログラムが応答しない

- **対処法**：
  - 一度プログラムを終了し、再起動してください。
  - それでも解決しない場合、パソコンを再起動してみてください。

### Q4. キャプチャ中に誤ってPCを操作してしまった

- **対処法**：
  - キャプチャが正しく行われていない可能性があります。生成されたPDFを確認し、問題がある場合は再度キャプチャをやり直してください。

---

## アンインストール方法

- 本ソフトウェアはインストール不要のため、特別なアンインストール手順は必要ありません。
- プログラムを削除する場合、`ebook2pdf.exe`ファイルを削除してください。
- 生成されたPDFファイルや一時ファイルがある場合、必要に応じて削除してください。

---

## ライセンス

- **フリーソフトウェア**：本ソフトウェアは無料でご利用いただけます。
- **再配布**：商用・非商用問わず、自由に配布していただけます。
- **免責事項**：本ソフトウェアの使用により生じたいかなる損害についても、作者は一切の責任を負いません。**自己責任でご利用ください**。

---

## 更新履歴

- **バージョン 1.0**
  - 初回リリース

---

## お問い合わせ

- **作者**：音又ハル
- **連絡先**：otomata.haru@gmail.com

---


