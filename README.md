# skk-to-plist

SKKの辞書をMacのユーザー辞書でインポートできる`.plist`に変換するユーティリティー。

## 注意点

- 一旦辞書をすべてメモリ上に読み込みます。その為、メモリが極端に少ない場合や辞書が極端に大きい場合は変換に失敗する可能性があります。
- 送りがながあるエントリは無視されます。

## 必要なもの

- Python 3.x系(Homebrewなどでインストールしてください)
- `chardet`ライブラリ(`pip3 install chardet`でインストールできます)
- 変換元のSKK辞書(dic-src/に入れてください)

## 実行

```
python3 main.py
```
実行が終わるとdic-dist/にplistファイルが出力されています。

## 生成したplistファイルの使い方について

[Mac でユーザ辞書を書き出す／読み込む方法 - Apple サポート](https://support.apple.com/ja-jp/HT204006)  
ここよんで