import streamlit as st
from ocr_utils import extract_text
from text_processing import process_text, analyze_text
import io

def main():
    st.title('OCR テキスト抽出と分析ウェブアプリ')

    # ファイルアップローダーでユーザーが自分の画像を追加できます
    uploaded_file = st.file_uploader('画像を選択してください...', type=['jpg', 'jpeg', 'png'])

    if uploaded_file is not None:
        # アップロードされた画像を表示
        st.image(uploaded_file, caption='アップロードされた画像。', use_column_width=True)
        st.write('')
        st.write('処理中...')

        # ファイルを画像に変換
        image_bytes = uploaded_file.getvalue()

        # OCRを使用して画像からテキストを抽出
        extracted_text = extract_text(image_bytes)

        if extracted_text:
            st.write('抽出されたテキスト:')
            st.write(extracted_text)

            # 抽出されたテキストを処理
            processed_text = process_text(extracted_text)
            st.write('処理されたテキスト:')
            st.write(processed_text)

            # 処理されたテキストを分析
            analysis_result = analyze_text(processed_text)
            st.write('分析結果:')
            st.json(analysis_result)
        else:
            st.write('テキストを抽出できませんでした。別の画像を試してください。')

if __name__ == '__main__':
    main()
