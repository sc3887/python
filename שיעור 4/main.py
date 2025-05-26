import matplotlib.pyplot as plt
import numpy as np

months = ['ינואר', 'פברואר', 'מרץ', 'אפריל', 'מאי', 'יוני', 'יולי', 'אוגוסט', 'ספטמבר', 'אוקטובר', 'נובמבר', 'דצמבר']
temperatures = [5, 7, 10, 15, 20, 25, 30, 29, 24, 18, 12, 7]

plt.plot(months, temperatures, marker='o')


plt.title('שינוי בטמפרטורה לאורך זמן')
plt.xlabel('חודש')
plt.ylabel('טמפרטורה (°C)')


plt.xticks(rotation=45)  # סיבוב תוויות החודשים
plt.grid()
plt.show()