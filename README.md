# bg-remove

- Azure AI Visionを使用して、画像の背景を取り除きます。

## 前提
- Azureサプスクリプションを持っていること。
- Azure Computer Visionのインスタンスをデプロイしていること。
    - 2023年12月現在、背景削除機能はPreviewバージョンであり、日本リージョンでは利用できないのでご注意ください。
    - 利用可能のリージョンは、Microsoftのドキュメントを参照してください。
## 使い方
1. 設定ファイルの用意
    - config.json.sampleをコピーしてconfig.jsonを作成します。
    - endpointには、Azure Computer Visionのエンドポイントを指定します。
    - keyには、Azure Computer VisionのAPIキーを指定します。
    - いずれも、Azureのポータルから確認できます。
1. venvの作成
    - `python -m venv .venv`を実行します。
    - 続いて、`.venv\Scripts\activate`を実行します。
1. モジュールのインストール
    - `pip install -r requirements.txt`を実行します。
1. 画像ファイルの用意
    - inputフォルダに、背景を取り除きたい画像ファイルを配置します。
1. 実行
    - `python main.py`を実行します。
    - outputフォルダに、背景が取り除かれた画像ファイルが出力されます。

## Documentations
- [Azure Computer Vision](https://docs.microsoft.com/ja-jp/azure/cognitive-services/computer-vision/)
- [Azure Computer Vision API](https://learn.microsoft.com/ja-JP/azure/ai-services/computer-vision/how-to/background-removal?tabs=python)
