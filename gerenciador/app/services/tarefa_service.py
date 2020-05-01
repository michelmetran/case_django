from ..models import Tarefa

# Acho que o erro pode estar aqui, no objeto, mas tá igual ao vídeo.
def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo,
                          descricao=tarefa.descricao,
                          data_expiracao=tarefa.data_expiracao,
                          prioridade=tarefa.prioridade)
