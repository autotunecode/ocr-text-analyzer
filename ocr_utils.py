import pytesseract
from PIL import Image
import io

def extract_text(image_bytes):
    '''
    OCRを使用して画像ファイルからテキストを抽出します。

    パラメータ:
    image_bytes (bytes): バイト形式の画像データ。

    戻り値:
    str: 画像から抽出されたテキスト。
    '''
    try:
        # バイトデータを画像に変換
        image = Image.open(io.BytesIO(image_bytes))
        # pytesseractを使用して画像上のOCRを実行
        text = pytesseract.image_to_string(image, lang='jpn')
    except Exception as e:
        print(f'OCR処理中にエラーが発生しました: {e}')
        return ''
    
    return text
