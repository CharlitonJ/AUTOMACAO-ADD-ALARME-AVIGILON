# Automador de Cadastro de Alarmes por Câmera

Este script foi desenvolvido para automatizar o fluxo de configuração de alarmes vinculados a câmeras em sistemas de monitoramento de segurança. O objetivo é padronizar a nomenclatura e ativar os alertas de forma sequencial, eliminando falhas manuais em processos repetitivos.

## Funcionamento do Script

1. **Entrada de Dados:** O usuário define o nome da unidade e o número total de câmeras a serem configuradas.
2. **Reconhecimento de Imagem:** O script utiliza capturas de tela para localizar botões, campos de busca e ícones de ativação.
3. **Padronização:** Gera nomes automáticos seguindo o modelo "Unidade - CAM XX" e insere nos campos de alarme.
4. **Tratamento de Exceções:** Caso um elemento visual não seja encontrado, o script interrompe o processo e informa ao usuário em qual ciclo ocorreu a falha.

## Pré-requisitos

Para executar este script, é necessário ter o Python instalado e as seguintes bibliotecas:

```bash
pip install pyautogui pyperclip opencv-python

O pacote opencv-python é essencial para habilitar o parâmetro de confiança (confidence) na busca pelas imagens.

## Lista de Arquivos de Imagem Necessários
O script busca pelos seguintes arquivos (formato .png) na mesma pasta do código:

Navegação Inicial: add.png, detec.png, soft_ext.png, seg.png, pesquisar.png.

Seleção de Dispositivo: check_box.png, visualizar_dispositivos.png, unid.png.

Comandos de Ação: add_dist.png, adm.png, add2.png, reproduzir.png.

Configuração de Alarme: alarme.png, novo.png, ativ.png, terminar.png.

##Instruções de Uso
Certifique-se de que o software de monitoramento esteja aberto e visível no monitor principal.

Execute o script via terminal ou IDE.

Insira as informações solicitadas (Nome da unidade e quantidade de câmeras).

Após o comando inicial, você terá 5 segundos para posicionar a janela correta na tela.

Não utilize o mouse ou o teclado enquanto o processo estiver em execução.

##Avisos e Segurança
Interrupção de Emergência (Failsafe): Caso precise parar o script imediatamente, mova o cursor do mouse para qualquer um dos quatro cantos da tela. Isso forçará a interrupção do programa.

Precisão Visual: O reconhecimento depende da resolução da tela e da escala (DPI) configurada no Windows. Recomenda-se utilizar 100% de escala para garantir que as imagens correspondam aos botões reais.

Limpeza de Campos: O código executa cliques duplos e a tecla Delete para garantir que campos de texto antigos sejam limpos antes da nova inserção.
