import plotly.express as px
import pandas as pd
import statistics as st
sudut = [0,5,10]
percepatan = [
                [   # Data percepatan sudut 0
                    [1.32,0.53,0.83,1.55,1.28], # l = 0,6m
                    [1.05,1.30,1.09,1.13,0.41], # l = 0,8m
                    [1.24,1.01,0.98,1.45,2.02]  # l = 1,0m
                ],  # Data percepatan sudut 5
                [   [0.41,1.15,0.49,0.43,0.51], # l = 0,6m
                    [0.42,0.72,0.60,0.51,0.45], # l = 0,8m
                    [0.82,0.90,0.54,0.89,1.25]  # l = 1,0m
                ],
                [   # Data percepatan sudut 10
                    [0.18,0.15,0.22,0.32,0.25], # l = 0,6m
                    [0.29,0.49,0.32,0.25,0.48], # l = 0,8m
                    [0.35,0.39,0.34,0.33,0.41]  # l = 1,0m
                ]
            ]
rata_rata = [0,0,0] # Inisialisasi lists
avg_buf = [0,0,0] # Inisialisasi lists
for x in range(3):
    for y in range(3):
        avg_buf[y] = st.mean(percepatan[x][y])
    rata_rata[x] = st.mean(avg_buf) # Hitung rata-rata percepatan untuk masing-masing sudut
    print(rata_rata[x])

#Buat data frame untuk grafik
df = pd.DataFrame({
    "Sudut (°)": sudut,
    "Percepatan (m/s²)": rata_rata,
})

#Buat grafik percepatan dan sudut
fig = px.line(df, x="Sudut (°)", y="Percepatan (m/s²)", title="Grafik percepatan dengan sudut", template="plotly_dark") 
fig.update_traces(line_color='#aa23ff', line_width=5)
fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 1
    )
)
fig.show()
