import re
from bpmn_python.bpmn_diagram_rep import BpmnDiagramGraph
from bpmn_python.bpmn_diagram_layouter import BpmnDiagramLayouter
from bpmn_python.bpmn_diagram_visualizer import BpmnDiagramVisualizer
from lxml import etree

class TextToBpmnConverter:
    def __init__(self, text):
        self.text = text
        self.bpmn_graph = BpmnDiagramGraph()
        self.bpmn_graph.create_new_diagram_graph(diagram_name="diagram1")
        self.process_id = self.bpmn_graph.add_process_to_diagram()

    def parse_text(self):
        # Divide o texto em fases
        phases = re.split(r'\n(?=PROCESSO)', self.text)

        for phase in phases:
            phase_lines = phase.strip().split("\n")
            phase_name = phase_lines[0]

            # Adicione a fase como um subprocesso no BPMN
            subprocess_id = self.bpmn_graph.add_subprocess_to_diagram(self.process_id, name=phase_name)

            # Para cada passo dentro da fase
            for step in re.split(r'\n(?=Passo)', "\n".join(phase_lines[1:])):
                if step.strip() == "":
                    continue

                step_lines = step.strip().split("\n")
                step_name = step_lines[0]

                # Adicione o passo como uma tarefa dentro do subprocesso
                task_id = self.bpmn_graph.add_task_to_diagram(subprocess_id, name=step_name)

                # Para cada item dentro do passo
                for item in step_lines[1:]:
                    if item.strip() == "":
                        continue

                    # Adicione o item como uma tarefa dentro da tarefa
                    self.bpmn_graph.add_task_to_diagram(task_id, name=item.strip())

    def create_bpmn(self):
        self.parse_text()
        BpmnDiagramLayouter.auto_layout_diagram(self.bpmn_graph)
        
    def visualize_bpmn(self):
        BpmnDiagramVisualizer.generate_visualization(self.bpmn_graph)