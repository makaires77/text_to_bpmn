import unittest
from text_to_bpmn import TextToBpmnConverter

class TestTextToBpmnConverter(unittest.TestCase):
    def test_init(self):
        converter = TextToBpmnConverter("FASE PREPARAR AMBIENTE DE DESENVOLVIMENTO")
        self.assertEqual(converter.text, "FASE PREPARAR AMBIENTE DE DESENVOLVIMENTO")

    def test_parse_text(self):
        converter = TextToBpmnConverter("FASE PREPARAR AMBIENTE DE DESENVOLVIMENTO")
        converter.parse_text()
        # Verificar se o gráfico BPMN foi construído corretamente

    def test_create_bpmn(self):
        converter = TextToBpmnConverter("FASE PREPARAR AMBIENTE DE DESENVOLVIMENTO")
        converter.create_bpmn()
        # Verificar se o gráfico BPMN foi construído e disposto corretamente

    def test_visualize_bpmn(self):
        converter = TextToBpmnConverter("FASE PREPARAR AMBIENTE DE DESENVOLVIMENTO")
        converter.visualize_bpmn()
        # Verificar se a visualização do gráfico BPMN foi gerada corretamente

if __name__ == '__main__':
    unittest.main()