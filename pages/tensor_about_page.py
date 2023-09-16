from .base_page import BasePage
from .locators import TensorAboutLocators


class TensorAboutPage(BasePage):
    """PageObject класс для страницы tensor.ru/about."""

    def should_be_working_block(self):
        """Проверка, что имеется раздел Работаем."""

        assert self.is_element_present(
            TensorAboutLocators.WORKING_SECTION
        ), "Раздел Работаем отсутствует"

    def should_be_same_height_and_width_photos(self):
        """Проверка, что у всех фото хронологии одинаковые высота и ширина."""

        first_image = self.find_element(TensorAboutLocators.IMAGE)
        first_image_height = first_image.size["height"]
        first_image_width = first_image.size["width"]

        images = self.find_elements(TensorAboutLocators.IMAGE)
        for image in images[1:]:
            assert (
                image.size["height"] == first_image_height
            ), "Высота изображения разная"
            assert (
                image.size["width"] == first_image_width
            ), "Ширина изображения разная"
