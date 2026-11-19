import matplotlib.pyplot as plt

# Constantes físicas (mesmos valores do relatório em LaTeX)
k = 8.99e9   # N·m²/C²
q1 = 1e-6    # 1 µC
q2 = 1e-6    # 1 µC


# Distâncias de 0,10 m até 1,00 m (passo de 0,01 m)
Campo = [0.10 + i * 0.01 for i in range(91)]
Raio = [k * abs(q1 * q2) / (r ** 2) for r in Campo]

plt.figure(figsize=(6, 4))
plt.plot(Campo, Raio, color="tab:blue", linewidth=2)
plt.title("Grafico da energia potencial")
plt.xlabel("Distância r (m)")
plt.ylabel("Campo(J)")
plt.grid(True)
plt.tight_layout()
plt.savefig("energia_potencial.png", dpi=150)
print("Gráfico salvo em energia_potencial.png!")
