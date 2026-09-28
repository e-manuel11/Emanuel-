import random
import tkinter as tk
from tkinter import messagebox, ttk

# --- DADOS ---
RESPOSTAS_PASTOR = [
    (
        "Como ter paz em tempos difíceis?",
        (
            "Filipenses 4:6-7 lembra-nos de não andarmos ansiosos por coisa"
            " alguma, mas apresentarmos os nossos pedidos a Deus. A paz que"
            " excede todo o entendimento guardará o vosso coração, diz o Pastor"
            " Emanuel Munjenje."
        ),
    ),
    (
        "Qual é o propósito da Oração?",
        (
            "A oração é o fôlego da alma e a nossa linha direta com o Criador."
            " Não é apenas pedir, mas alinhar a nossa vontade com a vontade de"
            " Deus."
        ),
    ),
    (
        "Como vencer a tentação?",
        (
            "Vigiando e orando, fugindo da aparência do mal e enchendo a mente"
            " com a Palavra de Deus, ensina o Pastor Emanuel."
        ),
    ),
    (
        "O que é a verdadeira Fé?",
        (
            "A fé é a certeza das coisas que se esperam e a convicção dos fatos"
            " que não se vêem (Hebreus 11:1)."
        ),
    ),
]

PERGUNTAS_BIBLIA = [
    (
        "Quem construiu a arca conforme a ordem de Deus?",
        ["Noé", "Moisés", "Abraão", "Davi"],
        0,
    ),
    (
        "Qual foi o primeiro milagre de Jesus registrado na Bíblia?",
        [
            "Curar um cego",
            "Transformar água em vinho",
            "Multiplicar os pães",
            "Andar sobre as águas",
        ],
        1,
    ),
    (
        "Quantos dias e noites Jesus jejuou no deserto?",
        ["7 dias", "12 dias", "40 dias", "100 dias"],
        2,
    ),
]


class AppUnificado(tk.Tk):

  def __init__(self):
    super().__init__()
    self.title("App Pr. Emanuel & Utilidades")
    self.geometry("360x580")
    self.configure(bg="#f0f4f8")

    style = ttk.Style()
    style.theme_use("clam")
    style.configure(
        "TNotebook.Tab", font=("Arial", 9, "bold"), padding=[5, 4]
    )

    self.notebook = ttk.Notebook(self)
    self.notebook.pack(fill="both", expand=True, padx=2, pady=2)

    # Abas
    self.tab_pastor = ttk.Frame(self.notebook)
    self.tab_biblia = ttk.Frame(self.notebook)
    self.tab_bantu = ttk.Frame(self.notebook)
    self.tab_calc = ttk.Frame(self.notebook)
    self.tab_macaco = ttk.Frame(self.notebook)

    self.notebook.add(self.tab_pastor, text="Pr. Emanuel")
    self.notebook.add(self.tab_biblia, text="Bíblia")
    self.notebook.add(self.tab_bantu, text="Bantu Bet")
    self.notebook.add(self.tab_calc, text="Calc")
    self.notebook.add(self.tab_macaco, text="Macaco")

    self.setup_aba_pastor()
    self.setup_aba_biblia()
    self.setup_aba_bantu()
    self.setup_aba_calc()
    self.setup_aba_macaco()

  # 1. Pr. Emanuel & WhatsApp
  def setup_aba_pastor(self):
    tk.Label(
        self.tab_pastor,
        text="Conselhos do Pr. Emanuel Munjenje",
        font=("Arial", 11, "bold"),
        fg="#1e3a8a",
        bg="#f0f4f8",
    ).pack(pady=8)

    self.txt_pastor = tk.Text(
        self.tab_pastor, height=6, width=32, font=("Arial", 9), wrap="word"
    )
    self.txt_pastor.pack(pady=2)
    self.txt_pastor.insert("1.0", "Selecione uma dúvida abaixo.")
    self.txt_pastor.config(state="disabled")

    for p, r in RESPOSTAS_PASTOR:
      tk.Button(
          self.tab_pastor,
          text=p,
          font=("Arial", 8),
          bg="#3b82f6",
          fg="white",
          width=36,
          command=lambda resp=r: self.mostrar_resp_pastor(resp),
      ).pack(pady=2)

    tk.Button(
        self.tab_pastor,
        text="💬 Atendimento WhatsApp\n(+244 922 479 827)",
        font=("Arial", 9, "bold"),
        bg="#22c55e",
        fg="white",
        command=lambda: messagebox.showinfo(
            "WhatsApp", "Envie mensagem para: +244922479827"
        ),
    ).pack(pady=10, fill="x", padx=15)

  def mostrar_resp_pastor(self, resp):
    self.txt_pastor.config(state="normal")
    self.txt_pastor.delete("1.0", tk.END)
    self.txt_pastor.insert("1.0", resp)
    self.txt_pastor.config(state="disabled")

  # 2. Bíblia Quiz
  def setup_aba_biblia(self):
    self.q_idx = 0
    self.lbl_q = tk.Label(
        self.tab_biblia,
        text="",
        font=("Arial", 10, "bold"),
        bg="#f0f4f8",
        wraplength=320,
    )
    self.lbl_q.pack(pady=15)

    self.btn_alt = []
    for i in range(4):
      b = tk.Button(
          self.tab_biblia,
          text="",
          font=("Arial", 9),
          bg="#e2e8f0",
          width=30,
          command=lambda idx=i: self.verificar_biblia(idx),
      )
      b.pack(pady=4)
      self.btn_alt.append(b)
    self.carregar_biblia()

  def carregar_biblia(self):
    p, alts, cor = PERGUNTAS_BIBLIA[self.q_idx]
    self.lbl_q.config(text=p)
    self.correta = cor
    for i, a in enumerate(alts):
      self.btn_alt[i].config(text=a)

  def verificar_biblia(self, idx):
    if idx == self.correta:
      messagebox.showinfo("Resultado", "Aleluia! Resposta Certa! 🙏")
    else:
      messagebox.showerror("Resultado", "Incorreto. Tente a próxima!")
    self.q_idx = (self.q_idx + 1) % len(PERGUNTAS_BIBLIA)
    self.carregar_biblia()

  # 3. Bantu Bet Cassino (Probabilidades)
  def setup_aba_bantu(self):
    tk.Label(
        self.tab_bantu,
        text="Simulador & Probabilidade (Bantu Bet)",
        font=("Arial", 10, "bold"),
        fg="#b91c1c",
        bg="#f0f4f8",
    ).pack(pady=10)

    self.b_var = tk.StringVar(value="Aviator (Crash)")
    for op in [
        "Aviator (Crash)",
        "Roleta (Vermelho/Preto)",
        "Futebol (Vitória Casa)",
    ]:
      tk.Radiobutton(
          self.tab_bantu,
          text=op,
          variable=self.b_var,
          value=op,
          bg="#f0f4f8",
          font=("Arial", 9),
      ).pack(anchor="w", padx=30, pady=3)

    tk.Button(
        self.tab_bantu,
        text="Simular Probabilidade",
        font=("Arial", 9, "bold"),
        bg="#1e3a8a",
        fg="white",
        command=self.simular_bantu,
    ).pack(pady=10)

    self.lbl_b_res = tk.Label(
        self.tab_bantu,
        text="Selecione um jogo e clique acima.",
        font=("Arial", 8),
        bg="white",
        relief="solid",
        width=38,
        height=5,
    )
    self.lbl_b_res.pack(pady=5)

  def simular_bantu(self):
    sel = self.b_var.get()
    if sel == "Aviator (Crash)":
      m = round(random.uniform(1.01, 14.5), 2)
      txt = (
          f"Aviator:\nAviãozinho voou até: {m}x\n(Jogue com"
          " responsabilidade!)"
      )
    elif sel == "Roleta (Vermelho/Preto)":
      c = random.choice(["Vermelho 🔴", "Preto ⚫", "Zero 🟢"])
      txt = f"Roleta:\nResultado simulado: {c}\nProbabilidade teórica: ~48.6%"
    else:
      p = random.randint(40, 85)
      txt = f"Futebol:\nChance estimada de vitória: {p}%\n(Boa sorte!)"
    self.lbl_b_res.config(text=txt)

  # 4. Calculadora
  def setup_aba_calc(self):
    self.visor = tk.Entry(
        self.tab_calc, font=("Arial", 14), justify="right", bd=3
    )
    self.visor.pack(pady=10, fill="x", padx=15)

    btns = [
        ("7", "8", "9", "/"),
        ("4", "5", "6", "*"),
        ("1", "2", "3", "-"),
        ("C", "0", "=", "+"),
    ]
    f_btns = tk.Frame(self.tab_calc, bg="#f0f4f8")
    f_btns.pack()
    for linha in btns:
      f = tk.Frame(f_btns, bg="#f0f4f8")
      f.pack(side="top")
      for c in linha:
        tk.Button(
            f,
            text=c,
            font=("Arial", 10, "bold"),
            width=6,
            height=2,
            bg="#e2e8f0",
            command=lambda ch=c: self.calc_click(ch),
        ).pack(side="left", padx=2, pady=2)

  def calc_click(self, ch):
    if ch == "C":
      self.visor.delete(0, tk.END)
    elif ch == "=":
      try:
        res = eval(self.visor.get())
        self.visor.delete(0, tk.END)
        self.visor.insert(0, str(res))
      except Exception:
        messagebox.showerror("Erro", "Expressão inválida")
    else:
      self.visor.insert(tk.END, ch)

  # 5. Jogo do Macaco & Banana
  def setup_aba_macaco(self):
    tk.Label(
        self.tab_macaco,
        text="🐵 Jogo do Macaco & Banana",
        font=("Arial", 11, "bold"),
        fg="#854d0e",
        bg="#f0f4f8",
    ).pack(pady=15)

    tk.Label(
        self.tab_macaco,
        text="Adivinhe o galho onde está a banana (1 a 10):",
        font=("Arial", 9),
        bg="#f0f4f8",
    ).pack(pady=5)

    self.macaco_alvo = random.randint(1, 10)
    self.txt_macaco = tk.Entry(
        self.tab_macaco, font=("Arial", 12), justify="center", width=5
    )
    self.txt_macaco.pack(pady=10)

    tk.Button(
        self.tab_macaco,
        text="Testar Palpite",
        font=("Arial", 9, "bold"),
        bg="#ca8a04",
        fg="white",
        command=self.jogar_macaco,
    ).pack(pady=5)

    self.lbl_m_res = tk.Label(
        self.tab_macaco, text="Boa sorte!", font=("Arial", 9), bg="#f0f4f8"
    )
    self.lbl_m_res.pack(pady=15)

  def jogar_macaco(self):
    try:
      p = int(self.txt_macaco.get())
      if p == self.macaco_alvo:
        self.lbl_m_res.config(
            text="🍌 Acertou! O macaco achou a banana!", fg="#16a34a"
        )
        self.macaco_alvo = random.randint(1, 10)
      elif p < self.macaco_alvo:
        self.lbl_m_res.config(
            text="📈 O galho é mais alto! Suba mais.", fg="#2563eb"
        )
      else:
        self.lbl_m_res.config(
            text="📉 O galho é mais baixo! Desça.", fg="#2563eb"
        )
    except ValueError:
      messagebox.showerror("Erro", "Introduza um número de 1 a 10.")


if __name__ == "__main__":
  app = AppUnificado()
  app.mainloop()
