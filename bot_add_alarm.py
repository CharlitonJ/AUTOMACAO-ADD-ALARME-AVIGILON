import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

print("O script iniciará em 5 segundos. Prepare a tela!")
time.sleep(5)

Unid=input("Digite o nome da unidade: ")

for n in range(1, 17):
    try:
        print(f"--- Iniciando Ciclo {n} de 16 ---")

        res = pyautogui.locateCenterOnScreen("add.png", confidence=0.6)
        pyautogui.click(res)
        
        res = pyautogui.locateCenterOnScreen("detec.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("soft_ext.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("seg.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("pesquisar.png", confidence=0.9)
        pyautogui.click(res)

        texto = f"{Unid} - CAM {n:02d}"
        pyperclip.copy(texto)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        res = pyautogui.locateCenterOnScreen("check_box.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("visualizar_dispositivos.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("seg.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("add_dist.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("adm.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("cdpsdn.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("add2.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("reproduzir.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("seg.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("seg.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("alarme.png", confidence=0.9)
        pyautogui.doubleClick(res)
        pyautogui.press('delete')

        res = pyautogui.locateCenterOnScreen("novo.png", confidence=0.9)
        pyautogui.doubleClick(res)
        pyautogui.press('delete')

        pyautogui.hotkey('ctrl', 'v')

        res = pyautogui.locateCenterOnScreen("ativ.png", confidence=0.9)
        pyautogui.click(res)

        res = pyautogui.locateCenterOnScreen("terminar.png", confidence=0.9)
        pyautogui.click(res)

        print(f"Ciclo {n} finalizado com sucesso.\n")
        time.sleep(1)

    except Exception as e:
        print(f"Erro no ciclo {n}: Imagem não encontrada ou interrupção manual.")
        break

print("PROCESSO FINALIZADO (16 ciclos concluídos ou interrompidos).")