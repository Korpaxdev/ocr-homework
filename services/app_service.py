import streamlit as st
from torch.cuda import OutOfMemoryError

from services.ocr_service import ocr_read_image
from utils.languages import DEFAULT_LANGUAGE, LANGUAGES_LIST
from utils.messages_utils import (CHOOSE_LANGUAGES, CHOOSE_MODE, CHOOSE_MODE_DESCRIPTION, DOWNLOAD_IMAGE,
                                  IGNORE_CASE_RESULT, IMAGE_READ_BUTTON, LOADING, NOT_FOUND_IMAGE_ERROR,
                                  NOT_FOUND_LANGUAGES, OUT_OF_MEMORY_ERROR, RESULT, TEXT_NOT_DETECTED_ERROR, TITLE, )
from utils.modes_utils import MODES_LIST


class IndexPage:
    def __init__(self, ):
        self.image_buffer = None
        self.mode = None
        self.languages = None

    def init_app(self, ):
        st.set_page_config(page_title=TITLE)
        st.title(TITLE)
        image = st.file_uploader(DOWNLOAD_IMAGE, )
        if image:
            self.image_buffer = image.read()
            st.image(self.image_buffer, width=300, )
        self.mode = st.radio(CHOOSE_MODE, MODES_LIST, )
        st.text(CHOOSE_MODE_DESCRIPTION)
        self.languages = st.multiselect(CHOOSE_LANGUAGES, LANGUAGES_LIST, default=DEFAULT_LANGUAGE, )
        button = st.button(IMAGE_READ_BUTTON)
        if button:
            self.submit_event()

    def submit_event(self, ):
        if not self.image_buffer:
            return st.error(NOT_FOUND_IMAGE_ERROR)
        if not self.languages:
            return st.error(NOT_FOUND_LANGUAGES)
        try:
            with st.spinner(LOADING):
                res = ocr_read_image(self.image_buffer, self.mode, self.languages, )
                if not res:
                    return st.error(TEXT_NOT_DETECTED_ERROR)
                string_res = " ".join(res)
            st.text_area(RESULT, string_res, )
            st.text_area(IGNORE_CASE_RESULT, string_res.lower(), )
        except OutOfMemoryError:
            st.error(OUT_OF_MEMORY_ERROR)
