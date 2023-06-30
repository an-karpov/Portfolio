## Кредитный скоринг
Датасет содержит информацию о клиентах некоторого банка.  

_Целевая переменная_ (таргет) – `SeriousDlqin2yrs`: клиент имел просрочку 90 и более дней

### Признаки
- `RevolvingUtilizationOfUnsecuredLines`: общий баланс средств (общий баланс по кредитным картам и личным кредитным линиям, за исключением недвижимости и долгов без рассрочки, таких как автокредиты, деленный на сумму кредитных лимитов)
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
```txt
├── README.md
├── data
│   ├── credit_scoring.csv       <- Original data
│   └── preprocessed_data.csv    <- Preprocessed data
│
├── app                <- Streamlit App.
│
├── models             <- Saved models.
│
├── pics               <- pictures
│
├── EDA_credit_scoring.ipynb
├── test-models.ipynb
│
└── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
                          generated with `pip freeze > requirements.txt`
```

## Запуск локально
### Shell

```shell
$ python -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ streamlit run app.py
```



### Описание
В качестве основной модели использовался **XGBClassifier**. Для подбора гиперпараметров использовалась Баессовская оптимизация (библиотека hyperopt). Для балансировки классов использовалась процедура "upsampling"

<img src="/pics/xgb_pipeline_score.png" alt="Alt text" title="Лучшее еачество модели">
