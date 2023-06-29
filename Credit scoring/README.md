## Кредитный скоринг
Датасет содержит информацию о клиентах некоторого банка.  

_Целевая переменная_ (таргет) – `SeriousDlqin2yrs`: клиент имел просрочку 90 и более дней

### Признаки
- `RevolvingUtilizationOfUnsecuredLines`: общий баланс средств (total balance on credit cards and personal lines of credit except real estate and no installment debt
like car loans divided by the sum of credit limits)
- `age`: возраст заемщика
- `NumberOfTime30-59DaysPastDueNotWorse`: сколько раз за последние 2 года наблюдалась просрочка 30-59 дней
- `DebtRatio`: ежемесячные расходы (платеж по долгам, алиментам, расходы на проживания) деленные на месячный доход
- `MonthlyIncome`: ежемесячный доход
- `NumberOfOpenCreditLinesAndLoans`: количество открытых кредитов (напрмер, автокредит или ипотека) и кредитных карт
- `NumberOfTimes90DaysLate`: сколько раз наблюдалась просрочка (90 и более дней)
- `NumberRealEstateLoansOrLines`: количество кредиов (в том числе под залог жилья)
- `RealEstateLoansOrLines`: закодированное количество кредиов (в том числе под залог жилья) - чем больше код буквы, тем больше кредитов
- `NumberOfTime60-89DaysPastDueNotWorse`: сколько раз за последние 2 года заемщик задержал платеж на 60-89 дней
- `NumberOfDependents`: количество иждивенцев на попечении (супруги, дети и др)
- `GroupAge`: закодированная возрастная группа - чем больше код, тем больше возраст


### Структура каталога
- '/data' -- папка с данными
- 'EDA_credit_scoring.ipynb' -- файл с развёрточным анализом данных (поиск аномалий, выбросов, пропусков)
- 'model.ipynb' -- файл с тестированием моделей, подбором их гиперпараметров
