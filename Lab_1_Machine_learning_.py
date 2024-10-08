{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns"
      ],
      "metadata": {
        "id": "wloWV-i527gf"
      },
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "aWGsuaJezDV8",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 270
        },
        "outputId": "5855f971-8fdb-4ab9-b6db-03a6bfdea393"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
              "0          1    15634602  Hargrave          619    France  Female   42   \n",
              "1          2    15647311      Hill          608     Spain  Female   41   \n",
              "2          3    15619304      Onio          502    France  Female   42   \n",
              "3          4    15701354      Boni          699    France  Female   39   \n",
              "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
              "\n",
              "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
              "0       2       0.00              1          1               1   \n",
              "1       1   83807.86              1          0               1   \n",
              "2       8  159660.80              3          1               0   \n",
              "3       1       0.00              2          0               0   \n",
              "4       2  125510.82              1          1               1   \n",
              "\n",
              "   EstimatedSalary  Exited  \n",
              "0        101348.88       1  \n",
              "1        112542.58       0  \n",
              "2        113931.57       1  \n",
              "3         93826.63       0  \n",
              "4         79084.10       0  "
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-62f59ee6-3bc4-403f-9cb6-d08af48eb467\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>15634602</td>\n",
              "      <td>Hargrave</td>\n",
              "      <td>619</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>101348.88</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>15647311</td>\n",
              "      <td>Hill</td>\n",
              "      <td>608</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>41</td>\n",
              "      <td>1</td>\n",
              "      <td>83807.86</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>112542.58</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>15619304</td>\n",
              "      <td>Onio</td>\n",
              "      <td>502</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>42</td>\n",
              "      <td>8</td>\n",
              "      <td>159660.80</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>113931.57</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>15701354</td>\n",
              "      <td>Boni</td>\n",
              "      <td>699</td>\n",
              "      <td>France</td>\n",
              "      <td>Female</td>\n",
              "      <td>39</td>\n",
              "      <td>1</td>\n",
              "      <td>0.00</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>93826.63</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>15737888</td>\n",
              "      <td>Mitchell</td>\n",
              "      <td>850</td>\n",
              "      <td>Spain</td>\n",
              "      <td>Female</td>\n",
              "      <td>43</td>\n",
              "      <td>2</td>\n",
              "      <td>125510.82</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>79084.10</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-62f59ee6-3bc4-403f-9cb6-d08af48eb467')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-46bdc22d-3057-4b6e-a0e4-70c3a25d0b13\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-46bdc22d-3057-4b6e-a0e4-70c3a25d0b13')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-46bdc22d-3057-4b6e-a0e4-70c3a25d0b13 button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-62f59ee6-3bc4-403f-9cb6-d08af48eb467 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-62f59ee6-3bc4-403f-9cb6-d08af48eb467');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ],
      "source": [
        "data = pd.read_csv('/content/Churn_Modelling - Churn_Modelling.csv')\n",
        "data.head()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.info()"
      ],
      "metadata": {
        "id": "s-KTd_As3J0O",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "5fd42acc-c122-46bd-881e-f9f8efed7873"
      },
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 10000 entries, 0 to 9999\n",
            "Data columns (total 14 columns):\n",
            " #   Column           Non-Null Count  Dtype  \n",
            "---  ------           --------------  -----  \n",
            " 0   RowNumber        10000 non-null  int64  \n",
            " 1   CustomerId       10000 non-null  int64  \n",
            " 2   Surname          10000 non-null  object \n",
            " 3   CreditScore      10000 non-null  int64  \n",
            " 4   Geography        10000 non-null  object \n",
            " 5   Gender           10000 non-null  object \n",
            " 6   Age              10000 non-null  int64  \n",
            " 7   Tenure           10000 non-null  int64  \n",
            " 8   Balance          10000 non-null  float64\n",
            " 9   NumOfProducts    10000 non-null  int64  \n",
            " 10  HasCrCard        10000 non-null  int64  \n",
            " 11  IsActiveMember   10000 non-null  int64  \n",
            " 12  EstimatedSalary  10000 non-null  float64\n",
            " 13  Exited           10000 non-null  int64  \n",
            "dtypes: float64(2), int64(9), object(3)\n",
            "memory usage: 1.1+ MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.isnull().sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Vxd6dYqA39IM",
        "outputId": "c5c80040-5fed-427a-bd71-c6cd7dc4da12"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RowNumber          0\n",
              "CustomerId         0\n",
              "Surname            0\n",
              "CreditScore        0\n",
              "Geography          0\n",
              "Gender             0\n",
              "Age                0\n",
              "Tenure             0\n",
              "Balance            0\n",
              "NumOfProducts      0\n",
              "HasCrCard          0\n",
              "IsActiveMember     0\n",
              "EstimatedSalary    0\n",
              "Exited             0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "No missing values"
      ],
      "metadata": {
        "id": "qEAhxFF844MO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.preprocessing import LabelEncoder\n",
        "for col in data.columns:\n",
        "  le=LabelEncoder()\n",
        "  data[col]=le.fit_transform(data[col])\n",
        "data.head(10)"
      ],
      "metadata": {
        "id": "eLnONNjd4mUR",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 427
        },
        "outputId": "6dcdd061-d048-410f-c519-d4f5f857fb7a"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "   RowNumber  CustomerId  Surname  CreditScore  Geography  Gender  Age  \\\n",
              "0          0        2736     1115          228          0       0   24   \n",
              "1          1        3258     1177          217          2       0   23   \n",
              "2          2        2104     2040          111          0       0   24   \n",
              "3          3        5435      289          308          0       0   21   \n",
              "4          4        6899     1822          459          2       0   25   \n",
              "5          5         312      537          254          2       1   26   \n",
              "6          6        1058      177          431          0       1   32   \n",
              "7          7        3589     2000            8          1       0   11   \n",
              "8          8        9066     1146          110          0       1   26   \n",
              "9          9        1054     1081          293          0       1    9   \n",
              "\n",
              "   Tenure  Balance  NumOfProducts  HasCrCard  IsActiveMember  EstimatedSalary  \\\n",
              "0       2        0              0          1               1             5068   \n",
              "1       1      743              0          0               1             5639   \n",
              "2       8     5793              2          1               0             5707   \n",
              "3       1        0              1          0               0             4704   \n",
              "4       2     3696              0          1               1             3925   \n",
              "5       8     2674              1          1               0             7531   \n",
              "6       7        0              1          1               1              513   \n",
              "7       4     2781              3          1               0             5978   \n",
              "8       4     4962              1          0               1             3718   \n",
              "9       2     4450              0          1               1             3550   \n",
              "\n",
              "   Exited  \n",
              "0       1  \n",
              "1       0  \n",
              "2       1  \n",
              "3       0  \n",
              "4       0  \n",
              "5       1  \n",
              "6       0  \n",
              "7       1  \n",
              "8       0  \n",
              "9       0  "
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-3cc35fd0-09de-4f60-b49f-671ce97b0675\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>RowNumber</th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>Surname</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>0</td>\n",
              "      <td>2736</td>\n",
              "      <td>1115</td>\n",
              "      <td>228</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>24</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>5068</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>1</td>\n",
              "      <td>3258</td>\n",
              "      <td>1177</td>\n",
              "      <td>217</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>23</td>\n",
              "      <td>1</td>\n",
              "      <td>743</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>5639</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2</td>\n",
              "      <td>2104</td>\n",
              "      <td>2040</td>\n",
              "      <td>111</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>24</td>\n",
              "      <td>8</td>\n",
              "      <td>5793</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>5707</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>3</td>\n",
              "      <td>5435</td>\n",
              "      <td>289</td>\n",
              "      <td>308</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>21</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>4704</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>4</td>\n",
              "      <td>6899</td>\n",
              "      <td>1822</td>\n",
              "      <td>459</td>\n",
              "      <td>2</td>\n",
              "      <td>0</td>\n",
              "      <td>25</td>\n",
              "      <td>2</td>\n",
              "      <td>3696</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>3925</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>5</th>\n",
              "      <td>5</td>\n",
              "      <td>312</td>\n",
              "      <td>537</td>\n",
              "      <td>254</td>\n",
              "      <td>2</td>\n",
              "      <td>1</td>\n",
              "      <td>26</td>\n",
              "      <td>8</td>\n",
              "      <td>2674</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>7531</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>6</th>\n",
              "      <td>6</td>\n",
              "      <td>1058</td>\n",
              "      <td>177</td>\n",
              "      <td>431</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>32</td>\n",
              "      <td>7</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>513</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>7</th>\n",
              "      <td>7</td>\n",
              "      <td>3589</td>\n",
              "      <td>2000</td>\n",
              "      <td>8</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>11</td>\n",
              "      <td>4</td>\n",
              "      <td>2781</td>\n",
              "      <td>3</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>5978</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>8</th>\n",
              "      <td>8</td>\n",
              "      <td>9066</td>\n",
              "      <td>1146</td>\n",
              "      <td>110</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>26</td>\n",
              "      <td>4</td>\n",
              "      <td>4962</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>3718</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9</th>\n",
              "      <td>9</td>\n",
              "      <td>1054</td>\n",
              "      <td>1081</td>\n",
              "      <td>293</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>9</td>\n",
              "      <td>2</td>\n",
              "      <td>4450</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "      <td>3550</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-3cc35fd0-09de-4f60-b49f-671ce97b0675')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-8a750bbd-ae0e-41a9-81a4-29a1ef6b7dc3\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-8a750bbd-ae0e-41a9-81a4-29a1ef6b7dc3')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-8a750bbd-ae0e-41a9-81a4-29a1ef6b7dc3 button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-3cc35fd0-09de-4f60-b49f-671ce97b0675 button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-3cc35fd0-09de-4f60-b49f-671ce97b0675');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data = data.drop([\"Surname\",\"RowNumber\"], axis=1)"
      ],
      "metadata": {
        "id": "DGbO2-I6Jd0Y"
      },
      "execution_count": 7,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data.describe()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 364
        },
        "id": "rkrvWknSBThK",
        "outputId": "6bd2f8ce-2162-4b67-f270-638ccc86e7e4"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "        CustomerId   CreditScore     Geography        Gender           Age  \\\n",
              "count  10000.00000  10000.000000  10000.000000  10000.000000  10000.000000   \n",
              "mean    4999.50000    259.584600      0.746300      0.545700     20.920600   \n",
              "std     2886.89568     96.496107      0.827529      0.497932     10.482065   \n",
              "min        0.00000      0.000000      0.000000      0.000000      0.000000   \n",
              "25%     2499.75000    193.000000      0.000000      0.000000     14.000000   \n",
              "50%     4999.50000    261.000000      0.000000      1.000000     19.000000   \n",
              "75%     7499.25000    327.000000      1.000000      1.000000     26.000000   \n",
              "max     9999.00000    459.000000      2.000000      1.000000     69.000000   \n",
              "\n",
              "             Tenure       Balance  NumOfProducts    HasCrCard  IsActiveMember  \\\n",
              "count  10000.000000  10000.000000   10000.000000  10000.00000    10000.000000   \n",
              "mean       5.012800   2036.788100       0.530200      0.70550        0.515100   \n",
              "std        2.892174   2125.232536       0.581654      0.45584        0.499797   \n",
              "min        0.000000      0.000000       0.000000      0.00000        0.000000   \n",
              "25%        3.000000      0.000000       0.000000      0.00000        0.000000   \n",
              "50%        5.000000   1383.500000       0.000000      1.00000        1.000000   \n",
              "75%        7.000000   3882.250000       1.000000      1.00000        1.000000   \n",
              "max       10.000000   6381.000000       3.000000      1.00000        1.000000   \n",
              "\n",
              "       EstimatedSalary        Exited  \n",
              "count     10000.000000  10000.000000  \n",
              "mean       4998.621200      0.203700  \n",
              "std        2886.711202      0.402769  \n",
              "min           0.000000      0.000000  \n",
              "25%        2498.750000      0.000000  \n",
              "50%        4998.500000      0.000000  \n",
              "75%        7498.250000      0.000000  \n",
              "max        9998.000000      1.000000  "
            ],
            "text/html": [
              "\n",
              "\n",
              "  <div id=\"df-146ff703-194f-4df8-9ed6-235bd05cf51a\">\n",
              "    <div class=\"colab-df-container\">\n",
              "      <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>CustomerId</th>\n",
              "      <th>CreditScore</th>\n",
              "      <th>Geography</th>\n",
              "      <th>Gender</th>\n",
              "      <th>Age</th>\n",
              "      <th>Tenure</th>\n",
              "      <th>Balance</th>\n",
              "      <th>NumOfProducts</th>\n",
              "      <th>HasCrCard</th>\n",
              "      <th>IsActiveMember</th>\n",
              "      <th>EstimatedSalary</th>\n",
              "      <th>Exited</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>count</th>\n",
              "      <td>10000.00000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.00000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "      <td>10000.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>mean</th>\n",
              "      <td>4999.50000</td>\n",
              "      <td>259.584600</td>\n",
              "      <td>0.746300</td>\n",
              "      <td>0.545700</td>\n",
              "      <td>20.920600</td>\n",
              "      <td>5.012800</td>\n",
              "      <td>2036.788100</td>\n",
              "      <td>0.530200</td>\n",
              "      <td>0.70550</td>\n",
              "      <td>0.515100</td>\n",
              "      <td>4998.621200</td>\n",
              "      <td>0.203700</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>std</th>\n",
              "      <td>2886.89568</td>\n",
              "      <td>96.496107</td>\n",
              "      <td>0.827529</td>\n",
              "      <td>0.497932</td>\n",
              "      <td>10.482065</td>\n",
              "      <td>2.892174</td>\n",
              "      <td>2125.232536</td>\n",
              "      <td>0.581654</td>\n",
              "      <td>0.45584</td>\n",
              "      <td>0.499797</td>\n",
              "      <td>2886.711202</td>\n",
              "      <td>0.402769</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>min</th>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>25%</th>\n",
              "      <td>2499.75000</td>\n",
              "      <td>193.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>14.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>0.00000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>2498.750000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>50%</th>\n",
              "      <td>4999.50000</td>\n",
              "      <td>261.000000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>19.000000</td>\n",
              "      <td>5.000000</td>\n",
              "      <td>1383.500000</td>\n",
              "      <td>0.000000</td>\n",
              "      <td>1.00000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>4998.500000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>75%</th>\n",
              "      <td>7499.25000</td>\n",
              "      <td>327.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>26.000000</td>\n",
              "      <td>7.000000</td>\n",
              "      <td>3882.250000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>1.00000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>7498.250000</td>\n",
              "      <td>0.000000</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>max</th>\n",
              "      <td>9999.00000</td>\n",
              "      <td>459.000000</td>\n",
              "      <td>2.000000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>69.000000</td>\n",
              "      <td>10.000000</td>\n",
              "      <td>6381.000000</td>\n",
              "      <td>3.000000</td>\n",
              "      <td>1.00000</td>\n",
              "      <td>1.000000</td>\n",
              "      <td>9998.000000</td>\n",
              "      <td>1.000000</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>\n",
              "      <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-146ff703-194f-4df8-9ed6-235bd05cf51a')\"\n",
              "              title=\"Convert this dataframe to an interactive table.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M0 0h24v24H0V0z\" fill=\"none\"/>\n",
              "    <path d=\"M18.56 5.44l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94zm-11 1L8.5 8.5l.94-2.06 2.06-.94-2.06-.94L8.5 2.5l-.94 2.06-2.06.94zm10 10l.94 2.06.94-2.06 2.06-.94-2.06-.94-.94-2.06-.94 2.06-2.06.94z\"/><path d=\"M17.41 7.96l-1.37-1.37c-.4-.4-.92-.59-1.43-.59-.52 0-1.04.2-1.43.59L10.3 9.45l-7.72 7.72c-.78.78-.78 2.05 0 2.83L4 21.41c.39.39.9.59 1.41.59.51 0 1.02-.2 1.41-.59l7.78-7.78 2.81-2.81c.8-.78.8-2.07 0-2.86zM5.41 20L4 18.59l7.72-7.72 1.47 1.35L5.41 20z\"/>\n",
              "  </svg>\n",
              "      </button>\n",
              "\n",
              "\n",
              "\n",
              "    <div id=\"df-1e48caad-93a9-48c6-abf6-3253c13741c8\">\n",
              "      <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-1e48caad-93a9-48c6-abf6-3253c13741c8')\"\n",
              "              title=\"Suggest charts.\"\n",
              "              style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "      </button>\n",
              "    </div>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "    background-color: #E8F0FE;\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: #1967D2;\n",
              "    height: 32px;\n",
              "    padding: 0 0 0 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: #E2EBFA;\n",
              "    box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: #174EA6;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "    background-color: #3B4455;\n",
              "    fill: #D2E3FC;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart:hover {\n",
              "    background-color: #434B5C;\n",
              "    box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "    filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "    fill: #FFFFFF;\n",
              "  }\n",
              "</style>\n",
              "\n",
              "    <script>\n",
              "      async function quickchart(key) {\n",
              "        const containerElement = document.querySelector('#' + key);\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      }\n",
              "    </script>\n",
              "\n",
              "      <script>\n",
              "\n",
              "function displayQuickchartButton(domScope) {\n",
              "  let quickchartButtonEl =\n",
              "    domScope.querySelector('#df-1e48caad-93a9-48c6-abf6-3253c13741c8 button.colab-df-quickchart');\n",
              "  quickchartButtonEl.style.display =\n",
              "    google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "}\n",
              "\n",
              "        displayQuickchartButton(document);\n",
              "      </script>\n",
              "      <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      flex-wrap:wrap;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "      <script>\n",
              "        const buttonEl =\n",
              "          document.querySelector('#df-146ff703-194f-4df8-9ed6-235bd05cf51a button.colab-df-convert');\n",
              "        buttonEl.style.display =\n",
              "          google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "        async function convertToInteractive(key) {\n",
              "          const element = document.querySelector('#df-146ff703-194f-4df8-9ed6-235bd05cf51a');\n",
              "          const dataTable =\n",
              "            await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                     [key], {});\n",
              "          if (!dataTable) return;\n",
              "\n",
              "          const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "            '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "            + ' to learn more about interactive tables.';\n",
              "          element.innerHTML = '';\n",
              "          dataTable['output_type'] = 'display_data';\n",
              "          await google.colab.output.renderOutput(dataTable, element);\n",
              "          const docLink = document.createElement('div');\n",
              "          docLink.innerHTML = docLinkHtml;\n",
              "          element.appendChild(docLink);\n",
              "        }\n",
              "      </script>\n",
              "    </div>\n",
              "  </div>\n"
            ]
          },
          "metadata": {},
          "execution_count": 8
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Checking For Correlation\n",
        "sns.heatmap(data.corr())\n",
        "plt.plot()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 552
        },
        "id": "l6xqb-i2JRW4",
        "outputId": "1e6e7a47-b06f-445d-cdda-7a872060f134"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "[]"
            ]
          },
          "metadata": {},
          "execution_count": 9
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 2 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.boxplot()\n",
        "plt.figure(figsize=(10,10))\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "q8jxV3KRG-a6",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "outputId": "b2989bec-04b6-45fb-8cd8-78b33e47cdf3"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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5woRERGpQrnP6Bw8eBBdunRRHpvCx+DBg7F69WpMmDABmZmZeOONN3D9+nV07NgR27Ztg729vfKcL774AiNHjkTXrl1hY2ODvn37YvHixcp4FxcXbN++HWFhYQgKCkLVqlUxdepUs+/aad++PdatW4cpU6Zg8uTJqFu3LrZs2YLGjRvf04wgIiIi9Sl30OncuTNEpMTxGo0GM2bMwIwZM0ps4+bmhnXr1pX6Ok2bNsUff/xRapvnn38ezz//fOkFExER0SOLv3VFREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKpl8aCTn5+Pf//73/D394fBYECdOnUwc+ZMiIjSRkQwdepUeHt7w2AwICQkBKdOnTLr5+rVqxg4cCCcnZ1RpUoVDB06FBkZGWZtjhw5gsceewz29vbw9fXFnDlzLD05REREZMUsHnRmz56NTz75BEuWLEF8fDxmz56NOXPm4KOPPlLazJkzB4sXL8ayZcsQHR0NR0dHhIaG4tatW0qbgQMH4tixY4iMjMTWrVuxa9cuvPHGG8r49PR0dO/eHX5+foiJicHcuXMxbdo0LF++3NKTRERERFbKztId7t27F71790avXr0AALVq1cKXX36J/fv3A7h9NiciIgJTpkxB7969AQBr1qyBp6cntmzZgv79+yM+Ph7btm3DgQMH0KpVKwDARx99hCeffBLz5s2Dj48PvvjiC+Tk5ODzzz+HTqdDo0aNEBsbiwULFpgFIiIiInp0WfyMTvv27bFjxw6cPHkSAHD48GHs3r0bPXv2BAAkJSUhJSUFISEhynNcXFzQtm1bREVFAQCioqJQpUoVJeQAQEhICGxsbBAdHa206dSpE3Q6ndImNDQUCQkJuHbtmqUni4iIiKyQxc/ovPvuu0hPT0eDBg1ga2uL/Px8zJo1CwMHDgQApKSkAAA8PT3Nnufp6amMS0lJgYeHh3mhdnZwc3Mza+Pv71+kD9M4V1fXIrVlZ2cjOztbeZyeng4AyM3NRW5u7j1Ps0leXp7yryX6qyim2ljj/bGGGgHrqJM1Wo411MkaLcca9jsVMS/L05fFg85XX32FL774AuvWrVM+ThozZgx8fHwwePBgS79cuYSHh2P69OlFhm/fvh0ODg733f/5DACww759+3Dh6H13V+EiIyMru4S7Yo2WYw11skbLsYY6WeP9s6b9jiXnZVZWVpnbWjzojB8/Hu+++y769+8PAGjSpAnOnj2L8PBwDB48GF5eXgCA1NRUeHt7K89LTU1F8+bNAQBeXl64dOmSWb95eXm4evWq8nwvLy+kpqaatTE9NrW506RJkzB27FjlcXp6Onx9fdG9e3c4Ozvfx1TfdvjcVSDuINq1a4dmNd3uu7+Kkpubi8jISHTr1g1arbayyykWa7Qca6iTNVqONdTJGi3HGvY7FTEvTZ/IlIXFg05WVhZsbMwv/bG1tUVBQQEAwN/fH15eXtixY4cSbNLT0xEdHY3hw4cDAIKDg3H9+nXExMQgKCgIAPDrr7+ioKAAbdu2Vdq89957yM3NVWZcZGQk6tevX+zHVgCg1+uh1+uLDNdqtRaZ+XZ2dsq/D/OKYWKp6a5IrNFyrKFO1mg51lAna7x/1rTfseS8LE8/Fr8Y+emnn8asWbPwww8/4MyZM9i8eTMWLFiAZ599FgCg0WgwZswYfPDBB/juu+8QFxeHl19+GT4+PujTpw8AIDAwED169MDrr7+O/fv3Y8+ePRg5ciT69+8PHx8fAMCAAQOg0+kwdOhQHDt2DBs2bMCiRYvMztgQERHRo83iZ3Q++ugj/Pvf/8aIESNw6dIl+Pj4YNiwYZg6darSZsKECcjMzMQbb7yB69evo2PHjti2bRvs7e2VNl988QVGjhyJrl27wsbGBn379sXixYuV8S4uLti+fTvCwsIQFBSEqlWrYurUqby1nIiIiBQWDzpOTk6IiIhAREREiW00Gg1mzJiBGTNmlNjGzc0N69atK/W1mjZtij/++ONeSyUiIiKV429dERERkWox6BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRajHoEBERkWox6BAREZFqMegQERGRaln8m5HVKulKJjKz80ptk3g5U/nX9ENrpXHU28G/qqNF6iMiIqKiGHTKIOlKJrrM21nm9uO+jitz29/e6cywQ0REZspycA2U7wD7UT24ZtApA9PCFtGvOQI8jCW3u5mNrTuj8FTnYDga9KX2efpSBsZsiC3TgkxERI+O8h5cA2U/wH4UD64ZdMohwMOIxtVdShyfm5uLlGpASz9XaLXaB1gZERGpRVkProGyH2A/ygfXDDpEREQPobsdXAM8wC4L3nVFREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqZVfZBRARPWyysrJw4sQJs2EZN7OxNy4RrlUPwmjQm41r0KABHBwcHmSJRFRGDDpERHc4ceIEgoKCih03p5hhMTExaNmyZcUWRUT3hEGHiOgODRo0QExMjNmwhOTrGLsxDgueb4L63lWKtCeihxODDhHRHRwcHIqcobE5+w/0f9xEYONmaO7nXkmVEVF58WJkIiIiUi0GHSIiIlItBh0iIiJSLQYdIiIiUi0GHSIiIlItBh0iIiJSrQoJOhcuXMBLL70Ed3d3GAwGNGnSBAcPHlTGiwimTp0Kb29vGAwGhISE4NSpU2Z9XL16FQMHDoSzszOqVKmCoUOHIiMjw6zNkSNH8Nhjj8He3h6+vr6YM6e4r/IiIiKiR5XFg861a9fQoUMHaLVa/PTTTzh+/Djmz58PV1dXpc2cOXOwePFiLFu2DNHR0XB0dERoaChu3bqltBk4cCCOHTuGyMhIbN26Fbt27cIbb7yhjE9PT0f37t3h5+eHmJgYzJ07F9OmTcPy5cstPUlERERkpSz+hYGzZ8+Gr68vVq1apQzz9/dX/i8iiIiIwJQpU9C7d28AwJo1a+Dp6YktW7agf//+iI+Px7Zt23DgwAG0atUKAPDRRx/hySefxLx58+Dj44MvvvgCOTk5+Pzzz6HT6dCoUSPExsZiwYIFZoGIiIiIHl0WDzrfffcdQkND8fzzz+P3339H9erVMWLECLz++usAgKSkJKSkpCAkJER5jouLC9q2bYuoqCj0798fUVFRqFKlihJyACAkJAQ2NjaIjo7Gs88+i6ioKHTq1Ak6nU5pExoaitmzZ+PatWtmZ5BMsrOzkZ2drTxOT08HAOTm5iI3N7fEacrLy1P+La2daVxpbcrbZ0UoT52VhTVajjXUaQ01VuY6Wx7WMC9ZY+nKs6yVtU617XPK05fFg85ff/2FTz75BGPHjsXkyZNx4MABvPXWW9DpdBg8eDBSUlIAAJ6enmbP8/T0VMalpKTAw8PDvFA7O7i5uZm1KXymqHCfKSkpxQad8PBwTJ8+vcjw7du3l/rLw+czAMAOu3fvxllj6dMPAJGRkXdtU94+K0JZ6qxsrNFyrKHOh7lG0zq7b98+XDha2dXc3cM8L01YY/HuZf9wtzrVts/Jysoqc1uLB52CggK0atUKH374IQCgRYsWOHr0KJYtW4bBgwdb+uXKZdKkSRg7dqzyOD09Hb6+vujevTucnZ1LfN6xi+mYF7cPHTt2RCOfktvl5uYiMjIS3bp1g1arLbWWsvZZEcpTZ2VhjZZjDXVaQ42Hz10F4g6iXbt2aFbTrbLLKZE1zEvWWLry7B/KWqfa9jmmT2TKwuJBx9vbGw0bNjQbFhgYiE2bNgEAvLy8AACpqanw9vZW2qSmpqJ58+ZKm0uXLpn1kZeXh6tXryrP9/LyQmpqqlkb02NTmzvp9Xro9foiw7Vabakz387OTvm3LG/S3fq7lz4rQlnqrGys0XKsoc6HucaHYZ0tj4d5XpqwxuLdy7Jm6f1YRbDkvCxPPxa/66pDhw5ISEgwG3by5En4+fkBuH1hspeXF3bs2KGMT09PR3R0NIKDgwEAwcHBuH79OmJiYpQ2v/76KwoKCtC2bVulza5du8w+p4uMjET9+vWL/diKiIiIHj0WDzpvv/029u3bhw8//BCnT5/GunXrsHz5coSFhQEANBoNxowZgw8++ADfffcd4uLi8PLLL8PHxwd9+vQBcPsMUI8ePfD6669j//792LNnD0aOHIn+/fvDx8cHADBgwADodDoMHToUx44dw4YNG7Bo0SKzj6aIiIjo0Wbxj65at26NzZs3Y9KkSZgxYwb8/f0RERGBgQMHKm0mTJiAzMxMvPHGG7h+/To6duyIbdu2wd7eXmnzxRdfYOTIkejatStsbGzQt29fLF68WBnv4uKC7du3IywsDEFBQahatSqmTp3KW8uJiIhIYfGgAwBPPfUUnnrqqRLHazQazJgxAzNmzCixjZubG9atW1fq6zRt2hR//PHHPddJRERE6sbfuiIiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVsqvsAqxBdv4t2NhfQFJ6AmzsjSW2y8vLw8W8i4i/Gg87u9JnbVJ6BmzsLyA7/xYAFwtXTERERACDTplczDwLR/+PMHl/2dp/vO3jMrVz9AcuZjZHEDzvozoiIlKTsh5cA2U/wH6UD64ZdMrAx9EPmUmjsKhfc9TxKP2Mzp7de9ChY4e7ntFJvJSB0Rti4dPFz9LlEhGRFSvvwTVQtgPsR/XgmkGnDPS29ii4VR3+zvXR0L3kJJybm4skuyQEugVCq9WW2mfBrTQU3LoMva29pcslIiIrVtaDa6DsB9iP8sE1gw4REdFDpKwH10DZD7Af5YNr3nVFREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKpV4UHnP//5DzQaDcaMGaMMu3XrFsLCwuDu7g6j0Yi+ffsiNTXV7Hnnzp1Dr1694ODgAA8PD4wfPx55eXlmbXbu3ImWLVtCr9cjICAAq1evrujJISIiIitSoUHnwIED+PTTT9G0aVOz4W+//Ta+//57bNy4Eb///jsuXryI5557Thmfn5+PXr16IScnB3v37sV///tfrF69GlOnTlXaJCUloVevXujSpQtiY2MxZswYvPbaa/j5558rcpKIiIjIilRY0MnIyMDAgQOxYsUKuLq6KsPT0tKwcuVKLFiwAE888QSCgoKwatUq7N27F/v27QMAbN++HcePH8fatWvRvHlz9OzZEzNnzsTSpUuRk5MDAFi2bBn8/f0xf/58BAYGYuTIkfjXv/6FhQsXVtQkERERkZWxq6iOw8LC0KtXL4SEhOCDDz5QhsfExCA3NxchISHKsAYNGqBmzZqIiopCu3btEBUVhSZNmsDT01NpExoaiuHDh+PYsWNo0aIFoqKizPowtSn8EdmdsrOzkZ2drTxOT08HAOTm5iI3N7fE55k+MsvLyyu1nWlcaW3K22dFKE+dlYU1Wo411GkNNVbmOlse1jAvWWPpyrOslbVOte1zytNXhQSd9evX488//8SBAweKjEtJSYFOp0OVKlXMhnt6eiIlJUVpUzjkmMabxpXWJj09HTdv3oTBYCjy2uHh4Zg+fXqR4du3b4eDg0OJ03M+AwDssHv3bpw1lthMERkZedc25e2zIpSlzsrGGi3HGup8mGs0rbP79u3DhaOVXc3dPczz0oQ1Fu9e9g93q1Nt+5ysrKwyt7V40Dl//jxGjx6NyMhI2NvbW7r7+zJp0iSMHTtWeZyeng5fX190794dzs7OJT7v2MV0zIvbh44dO6KRT8ntcnNzERkZiW7dukGr1ZZaS1n7rAjlqbOysEbLsYY6raHGw+euAnEH0a5dOzSr6VbZ5ZTIGuYlayxdefYPZa1Tbfsc0ycyZWHxoBMTE4NLly6hZcuWyrD8/Hzs2rULS5Yswc8//4ycnBxcv37d7KxOamoqvLy8AABeXl7Yv3+/Wb+mu7IKt7nzTq3U1FQ4OzsXezYHAPR6PfR6fZHhWq221JlvZ2en/FuWN+lu/d1LnxWhLHVWNtZoOdZQ58Nc48OwzpbHwzwvTVhj8e5lWbP0fqwiWHJelqcfiwedrl27Ii4uzmzYq6++igYNGmDixInw9fWFVqvFjh070LdvXwBAQkICzp07h+DgYABAcHAwZs2ahUuXLsHDwwPA7VNezs7OaNiwodLmxx9/NHudyMhIpQ8iorJKupKJzOy8UtskXs5U/jXtNErjqLeDf1VHi9RHRPfO4kHHyckJjRs3Nhvm6OgId3d3ZfjQoUMxduxYuLm5wdnZGaNGjUJwcDDatWsHAOjevTsaNmyIQYMGYc6cOUhJScGUKVMQFhamnJF58803sWTJEkyYMAFDhgzBr7/+iq+++go//PCDpSeJiFQs6UomuszbWeb2476Ou3uj/++3dzoz7BBVsgq766o0CxcuhI2NDfr27Yvs7GyEhobi448/Vsbb2tpi69atGD58OIKDg+Ho6IjBgwdjxowZSht/f3/88MMPePvtt7Fo0SLUqFEDn332GUJDQytjkojISpnO5ET0a44Aj5Kv0sy8mY2tO6PwVOdgOBqKfgRe2OlLGRizIfauZ4mIqOI9kKCzc+dOs8f29vZYunQpli5dWuJz/Pz8inw0dafOnTvj0KFDliiRiB5xAR5GNK7uUuL43NxcpFQDWvq5PvTXlRDR//C3roiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLXsKrsAa3AzNx8AcPRCWqntMm9m4+BlwOvsNTga9KW2PX0pw2L1ERERUfEYdMog8f+Hkne/iStDazv83+kDZe7bUc+3gIiI/qesB9dA2Q+wH+WDa+5ly6B7Iy8AQB0PIwxa2xLbJSSnYdzXcZj/ryao7+1y134d9Xbwr+posTqJiMj6le/gGijPAfajeHD96E3xPXBz1KF/m5p3bZeXlwcAqFPNEY2r3z3oEBER3amsB9dA+Q6wH9WDawYdIiKih0hZD64BHmCXBe+6IiIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1WLQISIiItVi0CEiIiLVYtAhIiIi1bJ40AkPD0fr1q3h5OQEDw8P9OnTBwkJCWZtbt26hbCwMLi7u8NoNKJv375ITU01a3Pu3Dn06tULDg4O8PDwwPjx45VvgDTZuXMnWrZsCb1ej4CAAKxevdrSk0NERERWzOJB5/fff0dYWBj27duHyMhI5Obmonv37sjMzFTavP322/j++++xceNG/P7777h48SKee+45ZXx+fj569eqFnJwc7N27F//973+xevVqTJ06VWmTlJSEXr16oUuXLoiNjcWYMWPw2muv4eeff7b0JBEREZGVsvhvXW3bts3s8erVq+Hh4YGYmBh06tQJaWlpWLlyJdatW4cnnngCALBq1SoEBgZi3759aNeuHbZv347jx4/jl19+gaenJ5o3b46ZM2di4sSJmDZtGnQ6HZYtWwZ/f3/Mnz8fABAYGIjdu3dj4cKFCA0NtfRkERERkRWq8B/1TEtLAwC4ubkBAGJiYpCbm4uQkBClTYMGDVCzZk1ERUWhXbt2iIqKQpMmTeDp6am0CQ0NxfDhw3Hs2DG0aNECUVFRZn2Y2owZM6bEWrKzs5Gdna08Tk9PBwDk5uYiNzf3vqfV9NFaXl6eRfqrKKbaWOP9sYYaAeuoszJrLOt6W54aK3NbwPfbMqyhRsA69jsVMS/L01eFBp2CggKMGTMGHTp0QOPGjQEAKSkp0Ol0qFKlillbT09PpKSkKG0KhxzTeNO40tqkp6fj5s2bMBgMReoJDw/H9OnTiwzfvn07HBwc7m0iCzmfAQB22LdvHy4cve/uKlxkZGRll3BXrNFyrKHOyqjRtN7u3r0bZ413b1+WGsvbZ0Xg+20ZD3uN1rTfseS8zMrKKnPbCg06YWFhOHr0KHbv3l2RL1NmkyZNwtixY5XH6enp8PX1Rffu3eHs7Hzf/R8+dxWIO4h27dqhWU23++6vouTm5iIyMhLdunWDVqut7HKKxRotxxrqrMwaj11Mx7y4fejYsSMa+ZS8HShPjWXtsyLw/bYMa6gRsI79TkXMS9MnMmVRYUFn5MiR2Lp1K3bt2oUaNWoow728vJCTk4Pr16+bndVJTU2Fl5eX0mb//v1m/Znuyirc5s47tVJTU+Hs7Fzs2RwA0Ov10Ov1RYZrtVqLzHw7Ozvl34d5xTCx1HRXJNZoOdZQZ2XUWN71tiw1PgzbAr7flvGw1/gwLGtlZcl5WZ5+LH7XlYhg5MiR2Lx5M3799Vf4+/ubjQ8KCoJWq8WOHTuUYQkJCTh37hyCg4MBAMHBwYiLi8OlS5eUNpGRkXB2dkbDhg2VNoX7MLUx9UFERERk8TM6YWFhWLduHb799ls4OTkp19S4uLjAYDDAxcUFQ4cOxdixY+Hm5gZnZ2eMGjUKwcHBaNeuHQCge/fuaNiwIQYNGoQ5c+YgJSUFU6ZMQVhYmHJG5s0338SSJUswYcIEDBkyBL/++iu++uor/PDDD5aeJCIiIrJSFj+j88knnyAtLQ2dO3eGt7e38rdhwwalzcKFC/HUU0+hb9++6NSpE7y8vPDNN98o421tbbF161bY2toiODgYL730El5++WXMmDFDaePv748ffvgBkZGRaNasGebPn4/PPvuMt5YTERGRwuJndETkrm3s7e2xdOlSLF26tMQ2fn5++PHHH0vtp3Pnzjh06FC5ayQiIqJHA3/rioiIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFSLQYeIiIhUi0GHiIiIVItBh4iIiFTL4r9eTkRkTbLzb8HG/gKS0hNgY28ssV1eXh4u5l1E/NV42NmVvulMSs+Ajf0FZOffAuBi4YqJqDwYdIjokXYx8ywc/T/C5P1la//xto/L1M7RH7iY2RxB8LyP6ojofjHoENEjzcfRD5lJo7CoX3PU8Sj9jM6e3XvQoWOHu57RSbyUgdEbYuHTxc/S5RJROTHoENEjTW9rj4Jb1eHvXB8N3Uv+mCk3NxdJdkkIdAuEVqsttc+CW2kouHUZelt7S5dLROXEi5GJiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi17Cq7AKo4WVlZOHHiRJHhGTezsTcuEa5VD8Jo0JuNa9CgARwcHB5UiURERBWKQUfFTpw4gaCgoBLHzylmWExMDFq2bFlxRRERET1ADDoq1qBBA8TExBQZnpB8HWM3xmHB801Q37tKkecQERGpBYOOijk4OBR7dsbm7D/Q/3ETgY2bobmfeyVURkRE9GAw6KhI0pVMZGbn3bVd4uVM5V87u9IXAUe9HfyrOlqkPiIiogeNQUclkq5kosu8neV6zriv48rU7rd3OjPsEBGRVWLQUQnTmZyIfs0R4GEsve3NbGzdGYWnOgfD8Y67rgo7fSkDYzbEluksERER0cOIQUclsvNvwcb+Amztq8HGvvSgY7DLg4/rRRicUmBTykdXtvYZsLG/gOz8WwBcLFwxERFRxWPQUYmLmWfh6P8RJu8v+3M+3vbxXds4+gMXM5sjCJ73UR0REVHlYNBRCVddDWQmjcKoLgF3/ejqZnYO/jgYh8daNYFBryux3fmrWZgXeRI+XfwsXS49IKtWrcKQIUOUx59//jleffXVSqyIiOjBYtBRib//yUPBrepY9NNNADfL8Iya+P50WhnaVYebQ+nBiR5OGo2myLAhQ4ZgyJAhEJFKqIiI6MFj0FGJ7o28AAB1PIwwaG1LbZuQnIZxX8dh/r+aoL536dfe8PZy61RcyLlzPMOO+oSFheHjj//3kfSIESOwdOnSSqyIHnXFbYse9LbH6oPO0qVLMXfuXKSkpKBZs2b46KOP0KZNm8ou64Fzc9Shf5uaZWqbl3f7Lqo61RzRuDovMlabVatWlbkdP8ZSj+J2KB9//DE+/vhjhlqqFCUdcD3oAy2r/vXyDRs2YOzYsXj//ffx559/olmzZggNDcWlS5cquzSiSlP4mhwAyMnJwZYtW5CTk1NqO7JeZTmDR/QgPUzLpFUHnQULFuD111/Hq6++ioYNG2LZsmVwcHDA559/XtmlET1wWVlZ+PPPP82GxcTEIGr/QeyNS0TU/oNFfvssKyvrQZZIFSAsLEz5f3h4uFmwDQ8PL7YdUUW6M8SUdLD1oMKO1X50lZOTg5iYGEyaNEkZZmNjg5CQEERFRRX7nOzsbGRnZyuP09PTAQC5ubnIzc0t1+tnZWUhISHBbNjJ5DRkp5zG0VgdclLNPxKqX78+HBwcyvUa96u4GoHKrfNiWjq+jjtkNizzRhpOHzUfVlBQgEuXL2NjXDRsbMzzeEDjFnB0+l/dns56PNOwGQx2hoe2RkvXWVyNZ0/FY8WHE2DvZ68M6/BcB+X/iz+7/W/h8e+uXQm/uoEVUmNJdT5s7/eNm7e3CYfPXVU+1r15MwtnEk+ZtcvPy0dcXCJuYCds7cyvg6tVpy4Mhv+tN6f//8+s5OXllXvbUpzS5uPGHz5X3tPjBRl4dfb7ZvPSNO7zHz6HZ+gTVrfuWEONFVHnnaxpe154G/P8G+PMlslBs97DxuXzlfEzvtt0T+93edYrjVjph7cXL15E9erVsXfvXgQHByvDJ0yYgN9//x3R0dFFnjNt2jRMnz69yPB169aVe2FITEzEuHHjytx+/vz5qFOnTrle436Vt0ag4uvcdukiduvu/v095dVPOwJNHH0s0ldF1QhYrk5rqBGwjvc7KlWD9X+ZB5fslNNI+e+YMvfhNTgCeq+AIsPfa54HDwvs9/h+P/w1Apat807cnpvLysrCgAEDkJaWBmdn51LbWu0ZnXsxadIkjB07Vnmcnp4OX19fdO/e/a4z6k5ZWVno2LGj2bCMm9n4+Y8DCH2sNYx3/LRCZZ3RubNGoHLrbJ6Wjq/j6poNK+1oyqNatQd+xFcRNVq6zuJqzMm5hcvJf+OTaW8Xaa91cEJu1o0iw6d+uhE63f+OvqxhXlq6xnaZOWgSfwm1qzkqdyzevNkUZ55vYtbu9hmdODRp0uSuZ3QAwFFvi1rulrljsbT5WPjo+Pk3xhWZl4XHT1q81urWHWuosSLqvJM1bc/D33pJeVxRy6TpE5kyESuVnZ0ttra2snnzZrPhL7/8sjzzzDNl6iMtLU0ASFpamkVqysnJkS1btkhOTo5F+qso1lAna7w/AO769zB5mOelycNa44gRI5T3NDw83KzO8PBwZdyIESMqu1TFwzovC7OGGkUezjrv3NYUrtFS26Hy7L+t9mJknU6HoKAg7NixQxlWUFCAHTt2mH2URfQokrt8In238WQ9Cn9PzqRJk6DT6dCnTx/odDqzaxj5fTr0oNy5fSm8TJbWrqJY9UdXY8eOxeDBg9GqVSu0adMGERERyMzM5HeDEOH2RuRh+LIuqnglvdeFxxM9SA/TMmm1Z3QAoF+/fpg3bx6mTp2K5s2bIzY2Ftu2bYOnJ3+Akgi4vTEpfGsnd3jqJSIYMWKE2bARI0bwPadKU9Ky96CXSasOOgAwcuRInD17FtnZ2YiOjkbbtm0ruyQiokqxdOlSs2DLj6uosj0MB1tWH3SIiIiISsKgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqxaBDREREqsWgQ0RERKrFoENERESqZdW/dXW/TN/QWK6fey9Fbm4usrKykJ6eDq1Wa5E+K4I11MkaLcca6mSNlmMNdbJGy7GGOiuiRtN+uyzftPxIB50bN24AAHx9fSu5EiIiIiqvGzduwMXFpdQ2GnmEf/GtoKAAFy9ehJOTU6m/slpW6enp8PX1xfnz5+Hs7GyBCiuGNdTJGi3HGupkjZZjDXWyRsuxhjorokYRwY0bN+Dj4wMbm9Kvwnmkz+jY2NigRo0aFu/X2dn5oV3gCrOGOlmj5VhDnazRcqyhTtZoOdZQp6VrvNuZHBNejExERESqxaBDREREqsWgY0F6vR7vv/8+9Hp9ZZdSKmuokzVajjXUyRotxxrqZI2WYw11VnaNj/TFyERERKRuPKNDREREqsWgQ0RERKrFoENERESqxaCjIhqNBlu2bAEAnDlzBhqNBrGxsVi9ejWqVKlSqbU9TGrVqoWIiIgH8lqdO3fGmDFjHshr0f2ZNm0amjdvXtlllGrPnj1o0qQJtFot+vTp80Bfu/A25WGzc+dOaDQaXL9+/YE870FuU1955RWLvNcVUXNJy0RFbvfuZftt1UEnJSUFo0aNQu3ataHX6+Hr64unn34aO3bsuO++LbVSV2SNQMkrqq+vL5KTk9G4cWMAQF5eXrHtLl++jOHDh6NmzZrQ6XRwcHCAg4MD9Ho9PD090aFDB3zyySfIysqySL2VISUlBaNHj0ZAQADs7e1x/vx5LFq0yOqnKyoqCra2tujVq9cDe02NRlPq37Rp0x5YLYW98sorZnW4u7ujR48eOHLkSJmfu3v3brPhW7Zsscg3ppfF1q1b8fjjj8PJyQkODg5o3bo1Vq9eXaTd2LFj0bx5cyQlJWH16tXKdqrwdHfv3h2HDh0q8tySdpj3urMvqe/09HS89957aNCgAezt7eHl5YWQkBB88803yu8S/f3339DpdNDpdEV2Wr/99huefPJJuLu7w8HBAQ0bNsS4ceNw4cIFAMXvRNu3b4/k5OQSv0DuzuXD9DdhwoQSp2natGnQaDQwGAxFarx48SLS0tLQuXPnMs+je7F69WqsW7euQvrOz8/Hf/7zHzRo0AAGgwFubm5o27YtPvvssxLnV48ePcrU9zfffIOZM2cqjx/kwWVxrDbonDlzBkFBQfj1118xd+5cxMXFYdu2bejSpQvCwsIquzwA91Zjbm5umfsvra2trS28vLxgZ1f6l1/37dsXhw4dQnh4OKpUqQJPT0/07t0bCxYsQFRUFCZMmICtW7fil19+KXNdd5OTk1Pu55RnvhT2119/oUWLFti+fTs+/PBDHDp0CF5eXnjiiScsPl0VIT8/HwUFBcWOW7lyJUaNGoVdu3bh4sWLD6Se5ORk5S8iIgLOzs5mw955550HUkdhpuWpR48eSh07duyAnZ0dnnrqqTL1YW9vjz179iAvL68iSy3WRx99hN69e6NDhw6Ijo7GkSNH0L9/f7z55ptF5mdiYiKeeOIJ1KhRw+zo/JdffkFycjJ+/vlnZGRkoGfPniUGl3tdl8ri+vXraN++PdasWYNJkybhzz//xK5du9CvXz9MmDABaWlpAG7vwF944QUUFBTg7Nmzynv46aefIiQkBF5eXti0aROOHz+OZcuWIS0tDfPnzy/xdXU6Hby8vEoMpgUFBWbLh+nv3//+d6nT4+3tjVu3bhWZl//3f/+HmjVrlmPOPFxEBO+//z4WLlyImTNn4vjx4/jtt9/wxhtvKNNa3Pz68ssvy9S/m5sbnJycytT2XvYH5SZWqmfPnlK9enXJyMgoMu7atWuSlJQkAOTQoUNmwwHIb7/9JiIiV69elQEDBkjVqlXF3t5eAgIC5PPPPxcREQBmf48//riIiOTn58v06dOlevXqotPppFmzZvLTTz8pr2F63Q0bNoirq6sAkBYtWkhCQoLs379fgoKCxNHRUbp27SqXLl0SAPLxxx/L008/LTqdTtzd3UWv14uPj4/4+vqKXq8Xf39/GTNmjACQ9evXS6dOnUSr1Uq9evVEq9UKAPnmm28EgGzevFlWrVol3t7eAkA6d+4skydPLjI9gwcPVubHzp07JTQ0VGrUqFHi/Hz99dfFw8NDdDqdVKlSRZydncXJyUm6dOki8+bNk4YNG4pOpxM/Pz957rnnpHbt2kqN7u7uMmPGDBk0aJA4OTlJnz59pEOHDqLT6cRgMCjT8OSTT0pGRoYyD03TqtfrZdWqVXLlyhXp37+/+Pj4iMFgkMaNG8u6devMan388cclLCxMwsLCxNnZWbRarTg5OcmNGzeUNn5+fjJr1ix59dVXxdHRUXx9fWXhwoUydOhQqVq1qtja2kr16tUlNjZWec4777wjAGTixIni5+cnzs7O0q9fP0lPT1faZGRkyKBBg8TR0VG8vLxk3rx58vjjj8vo0aOVNrdu3ZJx48aJj4+PODg4SJs2bZTlUURk1apV4uLiIt9++60EBgaKra2tJCUlFXlPbty4IUajUU6cOCH9+vWTWbNmmY3/9ttvJSAgQPR6vXTu3FlWr14tAOTatWtKmz/++EM6duwo9vb2UqNGDRk1alSx739JTLUWtmLFCmnQoIHo9XqpX7++LF26VBlnel83bdoknTt3FoPBIE2bNpW9e/cqbd5//31p1qyZWZ8LFy4UPz8/5fHgwYOld+/e8sEHH4i3t7fUqlVLBg8eLN27d5fnn39eXFxcxNXVVTp06CAA5NKlSyIiMmHCBKlbt64YDAbx9/eXKVOmSE5OjgwePFieeuopqVq1qlSrVk15nTlz5ggAcXd3F51OJ46OjhITE2NWFwBZsWKF9OnTR2xtbcXR0VFeeukl8fDwEBcXF5k+fbrExsZK7dq1BYBoNBqpW7eunD59WkREzp07J7a2tuLq6lpkni1evFgAyL59+5R5V/hv1apVxW7n9uzZIwBk27ZtZuuSp6en2NjYyKpVq8y2Y3Z2dgJANm7caLaO6fV6sbe3Fzs7OwkKClK2MXPmzJHGjRuLVqsVjUYjXbt2lYEDB0rv3r2lR48eAkAaNGgg9vb24ubmJs2aNZMWLVqITqcTNzc36d27t9jZ2Ymnp2eRadLpdDJkyBBp37692NraCgCxsbGRli1bSlJSkgwePLjIc+rVqydTpkxRlu+0tDSxsbGRp556SkaPHi3u7u7i6ekpbdq0EYPBIHXq1BF7e3tp166dtG7dWgCIXq8Xg8EgOp1OvL29ZdSoUfL++++Lo6Njkdfbs2ePGI1G0el0yn7BtNwOHjxYmZ9VqlSRjz76SGbPni2enp7i7u6u7BsKr3f16tUTe3t70Wq1YmdnJyEhIXLp0iX57bffiry2wWAQJycnee2112TMmDFm25HXXntNatWqJfb29tK0aVMZMWKE+Pr6isFgkI4dOwoAcXR0lJYtW4pWq5U6derItGnTil23TevYTz/9JB06dBAXFxdxc3OTXr16ydq1a0Wr1cquXbuU5Wv06NFSrVo1uXDhggwZMkT0er3Y2tpKvXr1pE6dOkWmw7T+mvZ3dnZ2YmdnV2Qb1LBhQ6lbt67Y29tLrVq1ZO3ateLn5ycLFy4sfqNUAqsMOv/8849oNBr58MMPS2xTlqATFhYmzZs3lwMHDkhSUpJERkbKd999JyIi+/fvFwDyyy+/SHJysvzzzz8iIrJgwQJxdnaWL7/8Uk6cOCETJkwQrVYrJ0+eNHvdunXrikajkTFjxki7du0kKChIOnfuLLt375Y///xTAgIC5M033xQA4uHhIa+//rpUq1ZNli1bJuvXrxcHBwdxdHSUOXPmyPbt26VGjRoCQGrVqiUbN26UevXqSceOHWXFihUCQJo2bSoAZPbs2WJjYyMTJ04UADJ+/HhxcXERBwcHASAJCQmSnJws169fl9zcXDEajTJs2DDRaDQSHh5eZD7m5+dLu3btpFGjRrJ9+3bp0KGDtGnTRiIiIuTkyZPy0ksvCQB59913JSEhQUaOHCkAZNCgQZKQkCDz588XAOLg4CDz5s2ThIQEqV27tnTo0EHs7e1l1KhRSu3+/v7yyiuvKPOwVq1asmnTJvnrr7/k4sWL8vfff8vcuXPl0KFDkpiYKIsXLxZbW1uJjo5W6n388cfFaDTK6NGjJSoqSjQajWi1Wlm+fLnSxs/PT9zc3GTp0qVy6tQpCQ8PFwDSpUsXOXDggMyfP1/0er24u7sr73v37t1Fo9HIc889J3FxcbJr1y7x8vKSyZMnK/0OHz5catasKb/88oscOXJEnnrqKXFycjILOq+99pq0b99edu3aJadPn5a5c+eKXq9Xlp9Vq1aJVquV9u3by549e+TEiROSmZlZ5H1ZuXKltGrVSkREvv/+e6lTp44UFBSIiMhff/0lWq1W3nnnHTlx4oR8+eWXUr16dbOgc/r0aXF0dJSFCxfKyZMnZc+ePdKiRQt55ZVXSlyn7nRn0Fm7dq14e3sr79mmTZvEzc1NVq9ebbZuNGjQQLZu3SoJCQnyr3/9S/z8/CQ3N1dEyh50jEajDBo0SI4ePSpHjx6VQYMGidFolCFDhsiRI0fkwIEDEhAQIFqtVm7evCkiIjNnzpQ9e/ZIUlKSfPfdd+Lp6SmzZ89WNuovvPCCaDQaOX/+vIiITJ8+XQBIfHy8jBgxQtzc3MTT01MJt6agU6NGDVm3bp08++yzotVqRavVyr59+2TlypUCQLRarTRs2FA2bdoko0ePFltbW9m5c6eIiAwcOFAAyGeffVZknmVnZyvLcl5eniQnJ4uzs7NERERIcnKyZGVlFbud+/PPPwWAfPfdd2brUufOnaVbt25y8eJFs+3Yf//7XwEgdnZ2smvXLpk7d67s2bNH3NzcJCgoSGxtbWX+/PlKWLOzs5MFCxbI3LlzxWg0ytKlS2XAgAHyzDPPKNuZBQsWSFJSkixZskQ0Go28++67cvz4cYmNjZWhQ4eKra2tGI1GJTD8+uuvMm3aNAEgbdq0ERsbG3nhhRdk69atsmTJEhk9erRcvnxZrl+/LkFBQdK2bVuJjIyUffv2SUREhNjY2Jgt31WrVhU7OzsZP368nDhxQvr06SMeHh5iY2MjY8eOlbi4OPHx8RF7e3slAHTu3Flq164tu3fvluXLl8v7778vjRo1End3d3Fzc5Pk5GRJTk6WoUOHSrdu3YoEHXt7e7G3t5eIiAhZsWKF2NnZiVarlZCQEDlx4oQSnP38/GTbtm1y/Phx8fPzk3r16knbtm1l0aJFUqtWLXF2dpY333xTsrOzJSIiQrRarTg4OMgzzzwj+/fvl61btyohybQd6dGjh2g0Glm5cqUkJiYqwW/YsGFm22UbGxvZvn27nD59Wp544gnp1KmTciBQmGmd+Prrr2XTpk1y6tQpOXTokDz99NPSpEkTeeedd8TPz08OHz6sLOPffvut5OTkyNSpU6Vly5byyiuvyNq1a8VgMCgHu8nJyfLCCy+I0WiUPn36iMFgkIkTJ8quXbtEo9FI/fr1lW2QaTkODAyUqKgoOXjwoLRv314MBsOjEXSio6OVsxglKUvQefrpp+XVV18t8/NFRHx8fIocPbdu3VpGjBhh9jzTWZRvvvlGvvzySwEgO3bsUJ4THh4u9evXFwAyZswYqVOnjnJ2omvXrvLhhx/KzJkzJTg4WERuBywAEhERIT///LPY2dnJhQsXlNS/ceNGASCPPfaYPPnkk2b19+vXTzkyKXxELyLy9ddfi5OTkwCQ+vXry6RJk+Tw4cMiIuLu7q5sCF577TX5448/xNnZWW7duqU8f8CAAWIwGOTTTz8VEZH27dtL06ZNpWHDhkobBwcH8fT0FBGRn376Sezs7OTFF1+UN954Q0REIiMjBYDMmjVLbGxs5MSJE8q03k2vXr1k3LhxyuPHH39cAgMDpaCgQPbt2ycA5Nlnn5XAwECljY2NjdjZ2Ymjo6NMmDBBWckWL14sIiI3b94UV1dX8fT0VKbLw8NDtFqt2Rmc8ePHS9u2bUXk9hkWnU4nX331lTL+n3/+EYPBoASds2fPiq2trVy4cMFsGrp27SqTJk0SkdvhAYDZ2aTitG/fXpk/ubm5UrVqVWW5njhxojRu3Nis/XvvvWf2/g8dOlSZ/yZ//PGH2NjYKMHgbu4MOoWXYZPCy7Bpmfzss8+U8ceOHVPChEjZg46np6dkZ2crwwofsZqWdW9vb9Hr9fLzzz8XW//cuXMlKChI2ai///774uDgIEOGDBERkc2bN4vppLepLicnJ/n++++VugDIlClTlLpq1qwpAJSzvG5ubqLX6yUnJ0dERPLy8sTR0VG+/PJLERFxdnYWBweHEudZ06ZNpWfPnso4FxcXWbVqlfL4zu3UtWvX5NlnnxWj0SgpKSnK+IiICBk8eLBy1kmj0ShnqUzreIsWLZTt2Keffiru7u5y8+ZNZR375JNPlCPyM2fOmL3/gwcPVs7mmMaLiAQHB8vAgQPNpm/AgAHKmV0/Pz/x8fGRVatWyfDhw8XZ2VlcXFzE19e32PdMRIqcJRURadeundny3ahRI7GxsVEOEgYMGKCcUXN0dBS9Xi8ajUYee+wxASABAQGSkZEhBoNBWV5M77mfn58YjUb5/fffJSMjQ5ycnGTGjBlFgo4paJiEhoZKlSpVpF27dmbv1XPPPae0uXPfsHHjRnFwcJD69euLyP8OfNzc3JRpOXv2rNjY2IiDg4Pk5+fLrVu3xMHBQVq1aqVsR1588UWpUaOGvPjiiyIiyn6i8LJ27NgxCQwMFBsbG2nSpIkMGzZMfvzxR+X9NC0rhf9M+7U///xTmjdvLr169SoyTXe+R2FhYeLg4KCEE9P6++qrr5ptg3r27Cl9+vRRtkGmg+j9+/crbeLj4wVAuYOOVV6jIxb6Mufhw4dj/fr1aN68OSZMmIC9e/eW2j49PR0XL15Ehw4dzIZ36NAB8fHxZsMCAgKU/3t6egIAmjRpYjbs0qVLyvDExEQMHToURqMRO3bswOTJk/Hvf/8b+/btg9FoxKRJkwAAjRs3Rnx8PHx9feHj46P017p1awDA+fPn0bZtW7NagoODS5ymvn37YuvWrQCAFi1aYOfOnWjZsiVWr16N/fv3Y9SoUdDpdHB0dMThw4eRkZEBd3d3GI1GGI1GrF+/Hrdu3UJiYiIAID4+Hp07d8apU6eQn58P4PbXf5s+h01ISICvry9OnTqF1atXw2g0onfv3gCA6dOno6CgAOfPnwcAtGrVyqzW/Px8zJw5E02aNIGbmxuMRiN+/vlnnDt3zqxdu3btzD6rr1+/vlk9Xl5eGDt2LBo1aoTs7GwcOXIEIoJ33nkHRqMRVatWRUZGBlJTU5GYmIg///wTly5dQq1atcw+d/b29lbew8TEROTk5JjNezc3N9SvX195HBcXh/z8fNSrV0+Zf0ajEb///rsy/4Db1xs0bdq0xPcsISEB+/fvx4svvggAsLOzQ79+/bBy5UplvGl5MGnTpo3Z48OHDyvz3/QXGhqKgoICJCUllfjaJcnMzDRbhk1/H3zwgdm0ATCbNm9vbwBQ5mNZNWnSBDqdTnl87do1ALevxSgoKIC9vT0uX76M7Oxs7N+/HwCwYcMGdOjQAV5eXjAajZgyZUqRZcfb2xv//e9/ER8fr1yrULduXYSHhyMuLg4ZGRlFnlN4eho3bgxnZ2dlekQEtWrVglarBXD72jl3d3dcunQJmZmZSE9PR1ZW1l3n2d20b98eRqMRrq6uOHz4MDZs2KBsd4D/rUtdunTBH3/8ARHB559/jtjYWHz22WcAgLZt2+L48eOYOXMmJk+ejLS0NFStWlVZx0zbkTZt2qBJkyZYunQpcnJylHl/5/vz/PPP4+DBg2jXrp0y/Pr16/jmm2/g6Oio1NSqVSusXLkSIgKNRgMHBwf8/fff6NChA95///0iF5SLCKKjo822A6b32MTNzQ1arRbfffcdAODs2bPQaDTo06cPYmNj8dJLL0Gj0SjPS0xMhJOTE27evIlNmzYVuVarVatWWLVqFTZu3Ih69erB19fXbHxOTg5EBCNHjlTexx07diA9PR1//fWXWdvCP4Pw999/AwAGDhwIJycnDBo0CFlZWUhNTTV7TrNmzeDg4ADg9nakoKAAWVlZcHJygqurK7KysnDw4EHMmTMHRqMRGzZswMWLF4ssR4Wv2WzYsCGOHj2Kffv2YciQIbh06RKefvppvPbaawBuLytbtmxB586d4erqCgDKBcXJycn44osvsG3bNgAwu5Zs6dKliImJwaeffgqj0Yjly5cXmZ9NmjRBXFyc2Tbot99+w5YtW1BQUICEhAR8++23sLW1RVBQkPK8Bg0a3NOdY6VfqfqQqlu3LjQaDU6cOFFiGxub2xmucCi68yK8nj174uzZs/jxxx8RGRmJrl27IiwsDPPmzbvvGmvXrq3UaNpAmDZ2wO27V0wXmZpqXbFiBdq2bYvGjRvjrbfeQmhoKGxsbODr64u///4bXbp0URY4S2rUqBE0Gg2aNWuGL7/8Eq+99href/99nD17Fr6+vkpoyMjIgLe3N3bu3Kk8t3fv3ujatSvGjx9f6mvceZFgRkYGhg0bhrfeegs3btxAy5YtERERgW7duinzxdHR0ew5c+fOxaJFixAREYEmTZrA0dERY8aMKfFitoCAAGg0GuVuDROtVgtvb28YDAalFq1Wq9QD3A4LTz/9NAYOHIgVK1bA399f2dAUnqaSLhQuTkZGBmxtbRETEwNbW1uzcUajUfm/wWAo9W6flStXIi8vzyzoigj0ej2WLFlS5loKT29h93KRZUZGBoD/LcOF3Tmtd64HAMzWhTsPZIq7ePbOZSM3NxdVqlTBgQMHlGH5+flo2bIl0tLSEBUVhYEDB2L69OkIDQ2Fi4sL1q9fX+QCV1PgmzRpEs6ePQsAWLRoEX788Ufs2LEDV65cUZY3U12Fp0er1ZotF7a2tsr6XXiaCwoKlHkGAD///LNZMLG1tUVOTg4SExPRpUuXItN/pw0bNqBhw4Zwd3cvdkdgml+Ojo6oU6cOAKBGjRoICAhQdrYAcO7cOSxatAitWrXC1atXsW7duiLr2LJly5CVlYW5c+fizz//RP369dGpUyflgCgzMxM//fQTtm/fjs2bN2Py5Mno1asX/P39sW7dOty6dQspKSmYOnUqCgoKcO7cOYgIOnbsiLS0NNSsWRMvvPACGjRogO3btyM8PBzz58/HqFGjANw+mEtOTsaKFSuU7cCgQYOwb98+pUYbGxvUrVsX69atQ//+/fHXX3/BYDCgSpUqCAgIgFarRatWrfDqq69i+PDh2L17N+Li4rBnzx58++23iIuLQ9euXZX+2rZtiyVLluDo0aMYMmRIkflrmj+Fl/8JEybgxo0bWL58uVlb0zJ/5swZTJ48GQCwZs0a+Pn5Yffu3Rg6dGip2xXTdiQ/Px8//vgjLl++jOeffx5r165F7dq1Ua1aNTzzzDPo1q3bXW8OsLGxQevWrdG6dWuMGTMGa9euxaBBg9C3b184Ojpi5MiR8PPzw+rVq+Hj44OCggI0btwYOTk5ZicGTBeZr1+/Hu+88w58fX3RqlUrzJgxA3PnzsWqVavMXtfR0RF///232TYoLy8PHTt2xHvvvYf4+HjlTmFLsMozOm5ubggNDcXSpUuRmZlZZPz169dRrVo1ALeTp0lxt4pXq1YNgwcPxtq1axEREaEslKajRdNZAABwdnaGj48P9uzZY9bHnj170LBhQ7NhLi4uSo03b94s8rqFb2uuUqUKfHx88NdffyEgIABBQUH4559/0LVrV3Tp0gUBAQGoVasWgNsLZmBgoLKymxw8eBDA7dvKo6OjzV6r8Aag8PSYuLu7o1u3bliyZAkyMzPRsGFDZb42bdoU2dnZuHbtGlq2bImUlBTY2dkhICAAAQEBaN68OU6cOIGqVasCAAIDA7Fz507Uq1dP2cFlZ2fDy8sLwO2zK+fPn0dgYCCOHz+OgIAAXL16FcDto+mAgACzI/U753Pv3r3x0ksvoVmzZqhduzZOnjxZpJ1p+k3TtWXLFtSpU6fIDtekZcuWyM3NhY2NjTJdvXr1QuvWrbFp0yasW7cOLVq0KPa5JnXq1IFWqzWb99euXTOrr0WLFsjPz8elS5eU1zH9mebP3eTl5WHNmjWYP38+YmNjlb/Dhw/Dx8cHX375JerXr68sDyaFA4Bpmk3z/86/kuZ/aTw9Pc2W4cJ//v7+Ze6nWrVqSElJMQs7ZfmKB3d3d2RmZsLDw0N53bp168LW1hYFBQXYu3cv/Pz88N5776FVq1aoW7euEmTu9J///Afff/89jh07BgB48skn0ahRI1y5cgVXrlwpV12Ojo64cOFCsWHN09MTHh4esLW1xTfffFNkni1btgyZmZnKmbvS+Pr6ok6dOmU62i1pOxYdHY2CggL07t0bzz33HP766y/4+Pgoy7BpO6LRaNChQwcMGzYMBQUF0Gq1yhmTevXqAQD8/f0xffp0dOzYEXl5edi8eTMyMjLw2WefYdy4cfD29sY777yDmjVrYuzYsXjssceQlpYGnU6H/Px8HDx4EG+++Sa++eYbjBs3DitWrFDOsN24cQP+/v5m2wHTWeDC6tevj23btuHYsWNITk6Gu7u7cganZcuWOHXqlDJtDRs2xLBhw7BmzRr8/vvviIqKUs7K6XQ6VKtWDY0aNcLRo0cxYMCAIq9lNBphZ2dntvw7OzvD0dGxxOU/JiZGWc5bt26NevXqFbl7UqfTQURw+PBhZT9i2o4YDAY89thjCA0NhV6vR0FBAYKDg5Xt8unTp4ucebob034sNzcXOTk5SEhIwJQpU9C1a1cEBgYqZ++Sk5Px9ttvIzw8HACU0Lpnzx60b98ePj4+yrqYmJgIjUZTZN9z5zaoQYMGGDp0KH766SesXbsWTz/9NPLy8hATE6M8JyEh4Z6+BsEqgw5w+/RYfn4+2rRpg02bNuHUqVOIj4/H4sWLERwcDIPBgHbt2uE///kP4uPj8fvvv2PKlClmfUydOhXffvstTp8+jWPHjmHr1q0IDAwEAHh4eMBgMGDbtm1ITU1VEuv48eMxe/ZsbNiwAQkJCXj33XcRGxuL0aNHl1jj8OHDAdw+PWqq8YMPPjBrO336dISHh2Px4sUYMmQI1qxZgz59+mDChAmIj4/H999/r7QNCQlBvXr1MHjwYJw+fRoAlP569eqFbdu2KYFt/fr12LZtG2xsbKDRaLB161ZcvnwZGRkZ+Oeff/DEE09g7dq1eOutt5CdnY369etjxowZePzxx5GQkIDz589Dq9Xihx9+gIigRYsW6Nq1K2bNmoUzZ84gJCQEkZGRePPNN3Hy5EkEBQXhyJEjyoZkwYIFyMrKUo5Ku3Xrhjp16iA1NRW7d+9G37598fbbbwMA9u/fj5EjR5b4ntetWxeRkZHYu3cv4uPjMWzYsCKneIHbR6Vjx45FQkICevbsiYyMDKSlpWHDhg2Ij49Hbm4uDh48iBMnTsDW1hYhISFwdHTE+vXrsX37dpw5cwZ79+6Fu7s7PvzwQ4iIslyUxGg0YujQoRg/fjx+/fVXHD16FK+88orZ0Xy9evUwcOBAvPzyy/jmm2+QlJSE/fv3Izw8HD/88EOp/Zts3boV165dw9ChQ9G4cWOzv759+2LlypUYNmwYTpw4gYkTJ+LkyZP46quvlO9kMR0hTZw4EXv37sXIkSMRGxuLU6dO4dtvvy11/t9N4WX45MmTiIuLw6pVq7BgwYIy99G5c2dcvnwZc+bMQWJiIpYuXYqffvrprs+rXbs2tFotevTogS1btiAyMhLPPfccbty4gXbt2qFu3bo4d+4c1q9fj8TERCxevBibN28utq8mTZpg4MCByun2+Ph4uLq64sqVK7Czs8OVK1fKXFf16tWRk5OD/v374+DBgzh16hQyMzOVneisWbNgY2ODhQsXYvjw4fjuu+8we/Zs9O7dGxMmTMC4ceOKnCGzhMLbMdNHcXFxcejcuTMiIyNRu3Zt5Ofno1mzZkhOTkZqaqpypnvlypU4ePAgqlevDr1ej5SUFOh0Ovz9999KeGzRogUWLlyIRo0a4ebNm9iwYQPq1q2LQ4cOQUSg0+ng7e2tfKzcs2dPbNq0CfPmzcPx48exd+9e5eBr48aNSE5OVs5+eHl5ITExEZs2bcLevXvxxhtvFPvxWfXq1eHl5aV8LGQ6MBoxYgT8/f1hZ2ennAGNiIjAqlWrMHjwYHz88ccwGAzKd/LUqlULu3btwtq1a3H06NESw6SXl5fZ8n/t2jWcO3euxOU/ICBAWcbOnDmD//u//8OyZcvM2tSqVQt5eXnIysrCSy+9hJiYGJw+fRr29vbQ6XTYsmULrly5ghdffBFvvvkm3n77bSQmJiI0NBQ//fQT+vfvj1OnThW7rP/rX//CwoULER0djbNnz2Lnzp0ICwtDvXr14OLigoKCAri6umLRokWIiorC119/rZxVi4iIQGhoKJ5//nkAwKlTpzB//nzUrVsXBw8exNWrV3Ht2jX8+9//xoEDB6DT6bBr1y5cuHABt27dAlD8NqhWrVr45ZdfsG3bNowdOxY9evTAsGHDEB0djZiYGLz22mvKmfhyKdcVPQ+ZixcvSlhYmPj5+YlOp5Pq1avLM888o1yUefz4cQkODhaDwSDNmzeX7du3m12MPHPmTAkMDBSDwaDc9vjXX38p/a9YsUJ8fX3FxsbG7PbyadOmSfXq1UWr1ZZ4e7np4sCLFy9Knz59lFsnTTVOnDhRXFxcBLh9S7iIyBdffCHNmzcXnU4nRqNRnJ2dRafTibOzszRr1sys34SEBOnYsaNya/bXX3+t9LVy5Urx8vISANKpUyeZN2+euLi4yIwZM8TLy0s0Go0MHjxYbt26Je+++660bNlSXFxcxGAwSJUqVaRKlSqi1WrFaDRKmzZtZPr06TJo0CDlVkA3Nzdxc3MTrVYrvr6+8thjj0ndunVFq9VKzZo15dlnny1ye3nhi8fi4+OlQ4cOotVqzS6G9Pf3l1mzZpV4Ifg///wjvXv3FqPRKB4eHjJlyhR5+eWXpXfv3kqbxx9/XEaMGCFvvvmmODs7i6urq7z11lsSFhYm/v7+yi2xNWvWlLlz5yoX+DVu3FjatGkjPj4+ynT169dP7O3tZcSIEWW6SPbGjRvy0ksvKRdfz5kzp8iFk6a7EmrVqiVarVa8vb3l2WeflSNHjohI8bdsF/bUU0/Jk08+Wew400X6hw8fLnJ7uelC0sIXGu/fv1+6desmRqNRHB0dpWnTpkUutC9NcbUWXoZdXV2lU6dOyk0DZblBQETkk08+EV9fX3F0dJSXX35ZZs2aVezt5YUVd9uxXq+XkJAQSUtLE5HbF4+7u7uL0WiUfv36ycKFC8XFxcXsYmTTe5yUlKSsW/b29lK3bl15/fXXxdbWVnQ6nVJX4fXX1E/hC4Yff/xxGThwoHTv3l0cHBzEyclJ9Hq9cgGzaZ75+/uLRqNR7oypU6eO8lUXhd3tYuQ7FR5feL4V3o6ZbuPeuHGj2Trm6uqq3Knk7OwsmzZtEgDSvn17qVatmvI1GKavZPD09FTuVHNwcFCmx2AwiNFoFI1GI7a2tvLcc88ptwhHRUVJ06ZNRafTCQD59ttvpXfv3spj01/NmjWVC9ajo6OVr+4AICNHjpTu3bubXYxsWu8mTJggAJTt551/BoNBuUhZo9GInZ2dtG7dWn755RdleTDVqNfrlYvTV61aVezt5YWXf9PXhdy5/A8YMEB5f0aMGKHUERoaKmvWrBEA4uzsrLSpV6+eMj9M83Lo0KEyefJks+1I06ZNlcfVqlWTRo0aSbVq1cRgMEj79u2L9Lt8+XLp0qWLVKtWTXQ6ndSsWVNeeeUVOXPmTLHrEwDx9fUVAOLq6ipXrlxRpmnevHmi0+lk//798sorryjryfDhw+Xdd9+VgIAAs3loWg6L2wb5+flJo0aNREQkOTlZevXqJXq9XmrWrClr1qy5p9vLNSIWurKX6B7t2bMHHTt2xOnTp5XrB+5V586d0bx5c4t8C+eZM2dQp04dHDhwAC1btrzv/irTrFmzsGzZsmJP8RMRPQxEBHXr1sWIESMwduxYi/VrlRcjk3XbvHkzjEYj6tati9OnT2P06NHo0KHDfYccS8nNzcU///yDKVOmoF27dlYZcj7++GO0bt0a7u7u2LNnD+bOnXtfH0sREVWky5cvY/369UhJScGrr75q0b4ZdOiBu3HjBiZOnIhz586hatWqCAkJKfXr3R+0PXv2oEuXLqhXrx6+/vrryi7nnpw6dQoffPABrl69ipo1a2LcuHHKVxQQET1sPDw8ULVqVSxfvtzidxfzoysiIiJSLau964qIiIjobhh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1GHSIiIhItRh0iIiISLUYdIiIiEi1/h9b9xoDlzrfYwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 1000x1000 with 0 Axes>"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# creditscore ,age, noofproducts, exited\n",
        "data.boxplot(column=['CreditScore','Age','NumOfProducts','Exited'])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "v8LxpL54co_C",
        "outputId": "b28b4aa5-413c-4cc8-dcc2-7a0c804cbd57"
      },
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 11
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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ZpJs1qxZdu2111piYqI98sgjZmY2f/58u/DCC83r9VrXrl1twoQJ5vf7A/tv27bNLr/8cvN6vdajRw/Ly8szSTZv3jwzM9u5c6dJsg8++CDw/6N/cnJy7JtvvjFJ9u67756wH998843dcccd1qFDB/N6vXbBBRfYggULAttfeeUVy8zMtPj4eEtPT7dp06YF7Z+enm6TJk2yW265xVq1amU5OTlmZvbvf//bBg4caAkJCda5c2cbPXp0vc8V6nfw4EFLTk62rVu32o033miTJ08O2v76669bt27dzOv12qBBg2zu3LkmKfDaM2MMzMxycnLsmmuusYyMDHvggQcC6+fNm2e1H22PPPKI9enTJ2i/6dOnW3p6etDjXHfddTZ58mTr0KGDtW7d2iZOnGh+v9/uv/9+O+uss6xTp0725z//ObDPrl27zOPx2NixY+u0a8aMGSbJVq1aVe97eM6cOUHv81rLly83SbZ48eLA9n/84x/2/e9/37xer82ZM8eqq6tt4sSJ1qlTJ4uPj7c+ffrYP//5z6D6V69ebX379jWv12v9+/e31157LaiuOXPmWOvWrYP2Ofo5q/XGG2/YRRddZF6v19q1a2fXX3+9mZn94Ac/qNMnM7NPP/3UrrnmGmvTpo0lJiZaZmamvfnmm8cfwGao9rVSn3feecc8Ho8tW7YssO53v/udtW/f3kpKSszsyHN3zz33BP5f3/NodvL39549e+yaa66xhIQEO/fcc+1vf/ubpaen2/Tp0xu9z5FEQDnGV199ZTExMfY///M/JywnyTp06GB//vOfbceOHfbZZ5/ZsmXLzOfz2dy5c23Hjh2Wl5dn5557rk2YMMHMzKqrq61nz5525ZVX2vr1623p0qV24YUXHjegVFVV2auvvmqSrLCw0IqLi23//v3m9/stOTnZxowZY4cPH663fdXV1TZgwAC74IILLC8vz3bs2GELFiywRYsWmZnZ2rVrLTY21iZNmmSFhYU2Z84ca9mypc2ZMyfwGOnp6ebz+WzatGm2ffv2wE9SUpJNnz7dtm3bZsuXL7cLL7zQbr311tN/8qPE7Nmz7aKLLjIzswULFth5551nNTU1Zmb2ySefmMfjsfvvv9+2bt1qL774onXq1CkooDAGR9R+Wbz22muWkJBgu3fvNrNTCyitWrWy3Nxc27p1q82ePdskWXZ2tk2ePNm2bdtmjz76qHk8nkAdTz75pEmyoqKiOu2qqKiw5ORku+eee6yqqsqKi4vN5/PZU089ZcXFxVZeXl5vQFm3bp1JsjfeeCOw/dxzz7VXX33VPvnkEysqKrInn3zSfD6fvfjii7Z161YbN26ceTwe27Ztm5kdCb/t27e3n/70p/bRRx/ZggUL7Dvf+U7IAWXhwoXWokULe/jhh23z5s22fv36wGfiV199ZZ07d7ZJkyZZcXGxFRcXm5nZ8OHDbciQIfbhhx8GPm+WLl0a2qA67kQBxczsgQcesPT0dNu/f7+tW7fO4uPj7fXXXw9sPzqgHO95bMj7e9iwYdanTx9buXKlrV271i699FJr2bIlAeVMt3r1apNkr7322gnLSbIxY8YErbvyyivrBJu//vWvds4555iZ2VtvvWVxcXH2xRdfBLb/85//PG5AMTuSyo/97dnsyNGPs846yxISEuzSSy+18ePH24YNGwLb33rrLYuNjbXCwsJ62//Tn/7UhgwZErTugQcesMzMzMByenp64LemWrfddpvdcccdQev+/e9/W2xsrH377bf11oVgl156qT311FNmZub3++3ss8+2d955x8zMHnzwQevZs2dQ+V//+tdBrwHG4IijvywGDBhg//Vf/2VmpxZQ0tPTrbq6OrCue/fudvnllweWq6qqLCkpyV588UUzM7vzzjvrfMkfrXfv3jZs2LDAcuvWrYPC/7Hv82+++cZ+/OMfW3JyspWUlAS2175OanXs2LHOEbeLL77Y7rrrLjMz++Mf/2jt2rULeh0888wzIQeUrKwsu/nmm4/bv/p+W+/Vq1fgl7EzVU5OjrVo0cKSkpKCfmrHpKKiwvr27Ws/+clPLDMz026//fag/Y8OKGb1P48ne38XFhaaJFuzZk1g+5YtW0zSGRdQmINyDAvhxroXXXRR0PKGDRs0adIkJScnB35uv/12FRcXq7y8XFu2bFFaWpo6duwY2CcrK+uU2jlixAgVFRXpjTfe0NVXX613331X/fr1C0zQW79+vTp37qzzzz+/3v23bNmiyy67LGjdZZddpo8//ljV1dUn7OPcuXOD+pidna2amhrt3LnzlPoSTQoLC7VmzRr9x3/8hyQpLi5ON954o2bPnh3YfvHFFwft873vfS9omTGo63e/+52ef/55bdmy5ZT2v+CCC4L+9HtKSop69eoV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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(y='Age', data=data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "kq9txXBPgIRv",
        "outputId": "b9f766ad-76a4-410d-a95b-6680c1288a17"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='Age'>"
            ]
          },
          "metadata": {},
          "execution_count": 12
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data['Age'].mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s70AdUlxgSiF",
        "outputId": "daa34a13-1e9c-446c-d5f3-d3add650d715"
      },
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "20.9206"
            ]
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df1=data[data['Age']<40]"
      ],
      "metadata": {
        "id": "-_Uy_4gCgdd3"
      },
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(y='Age', data=df1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "LBo56vVwgmuZ",
        "outputId": "3e432ad4-6671-4dd6-eada-da5fd2f30162"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='Age'>"
            ]
          },
          "metadata": {},
          "execution_count": 15
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df1['Age'].mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7ewL8WXYg0e0",
        "outputId": "020b01e9-ef04-4dba-bbc3-72693680ea4c"
      },
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "19.092455858747993"
            ]
          },
          "metadata": {},
          "execution_count": 16
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_9hSWmKthNw6",
        "outputId": "4fb99f27-6d77-45a5-dbb1-c31b9fd77362"
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(10000, 12)"
            ]
          },
          "metadata": {},
          "execution_count": 17
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df1.shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JQ9gbLBGhBiG",
        "outputId": "a4b225be-f527-4401-e568-c468c9713a15"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(9345, 12)"
            ]
          },
          "metadata": {},
          "execution_count": 18
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(y='NumOfProducts', data=data)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "ZHPhhfKyhtsX",
        "outputId": "1511679d-5409-41e9-bcbd-1f60994000a4"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='NumOfProducts'>"
            ]
          },
          "metadata": {},
          "execution_count": 19
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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lwQAAAhIyMrNL7/8ogULFqhjx46hekkAAICABXVaqnXr1jUWFPt8Ph07dkytWrXSG2+8EbJwAAAAgQqq3MybN69GuYmIiFDbtm01aNAgtW7dOmThAAAAAhVUubn77rtDHAMAACA06l1uPv3003q/aO/evYMKAwAA0FD1LjcJCQmy2Wzy+XySxEX8AABAWKr3r6XKysq0b98+lZWVafXq1YqPj9fChQtVUlKikpISLVy4UNdcc43eeeedi5kXAADgvOo9c9O5c2f/f99xxx1asGCBRowY4d/Wu3dvOZ1OzZkzR2lpaSENCQAAUF9BXedm165dio+PP2d7fHy8PvvsswaHAgAACFZQ5ebaa6+Vy+XSyZMn/dtOnjwpl8ula6+9NmThAAAAAhXUT8FzcnI0evRoderUyf/LqE8//VQ2m03vvvtuSAMCAAAEIqhyM3DgQO3bt09vvvmmvvjiC0nS2LFjddddd+myyy4LaUAAAIBABFVuJOmyyy7TvffeG8osAAAADRZ0ufn66681f/58ff7555KkHj16aOrUqbrmmmtCFg4AACBQQS0o3rBhg7p3767t27erd+/e6t27t7Zt26YePXqosLAw1BkBAADqLaiZm4cfflgzZszQU089dc722bNn6+abbw5JOAAAgEAFNXPz+eefa+LEieds/8tf/sJ1bgAAgKWCKjdt27ZVaWnpOdtLS0vVrl27hmYCAAAIWlCnpSZNmqR7771X+/btU1JSkiTpP//5j55++mllZGSENCAAAEAggio3c+bMUXR0tLKyspSZmSlJ6tChgx577DFNnTo1pAEBAAACEXC5OX36tJYtW6a77rpLM2bM0LFjxyRJ0dHRIQ8HAAAQqIDX3DRr1kz33XefTpw4IelMqQm22GzevFmjR49Whw4dZLPZlJ+ff97xmzZtks1mO+fhdruDen8AAGCeoBYUDxw4UCUlJQ1+88rKSvXp00fZ2dkBHbd3714dPnzY/2ARMwAAOCuoNTd/+9vfNHPmTB08eFD9+/c/535SZ2+meSGpqalKTU0N+P3btWunK664IuDjAACA+YIqN3feeack1Vg8bLPZ5PP5ZLPZVFVVFZp0dUhISJDX61XPnj312GOPaciQIXWO9Xq98nq9/ucej+eiZgMAANYKqtyUlZWFOke9tG/fXjk5Obruuuvk9Xq1ZMkSJScn66OP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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data['NumOfProducts'].mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1qn4uY_1hzka",
        "outputId": "da67adb2-202d-4e52-f862-86264500d3f4"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.5302"
            ]
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df1=df[df['NumOfProducts']<3.0]"
      ],
      "metadata": {
        "id": "j6Vrf0ash-0D"
      },
      "execution_count": 21,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(y='NumOfProducts', data=df1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "aZ1gedlHiHW1",
        "outputId": "1963e130-e8f7-49ab-b622-33688ed46c21"
      },
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='NumOfProducts'>"
            ]
          },
          "metadata": {},
          "execution_count": 22
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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YaFCQ0OrHcNsNstsNtdpnQAAwHc0qEtgVcnPz1dYWJgkKSAgQL169VJubq5ze0VFhXJzcxUXF+etEgEAgI/x6hmg4uJiHTt2zLleUFCg/Px8tWzZUvfee6+Sk5N1+vRprV69WpKUlpamyMhIdevWTdeuXdPy5cu1Y8cOff75584xrFarxo0bp969e6tPnz5KS0tTSUmJ864wAAAArwagAwcOaODAgc71m/Nwxo0bp8zMTJ09e1YnTpxwbi8rK9P06dN1+vRpNWnSRFFRUfriiy9cxhg1apTOnz+vlJQU2Ww2xcTEKCcnp9LEaAAAYFwmh8Ph8HYRvsZut8tisaioqEjBwcHeLgeAh1y9etX57LHs7GwFBQV5uSIAnlSb7+8GPwcIAACgtghAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcAhAAADAcNwKQDk5OdqzZ49zPT09XTExMXrqqaf0448/eqw4AACAuuBWAHrppZdkt9slSV9//bWmT5+uIUOGqKCgQFar1aMFAgAAeFojd3YqKChQ165dJUkbN27UsGHD9MYbb+jQoUMaMmSIRwsEAADwNLfOAAUEBOjKlSuSpC+++EKDBg2SJLVs2dJ5ZggAAMBXuRWA+vfvL6vVqtdee0379+/X0KFDJUnff/+92rVrV+Nxdu/ereHDhys8PFwmk0lZWVm37L9p0yY99thjat26tYKDgxUXF6fPPvvMpc+8efNkMplcli5dutT6GAEAwN3LrQD0zjvvqFGjRvr444+1bNkytW3bVpKUnZ2twYMH13ickpISRUdHKz09vUb9d+/erccee0zbtm3TwYMHNXDgQA0fPlyHDx926detWzedPXvWufz7hG0AAAC35gDde++92rJlS6X2xYsX12qcxMREJSYm1rh/Wlqay/obb7yhTz75RJ9++ql69OjhbG/UqJFCQ0NrVQsAADAOt84A+fv769y5c5XaL168KH9//zsuqqYqKip0+fJltWzZ0qX96NGjCg8P13333aenn35aJ06cuOU4paWl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vVwRAMAnlV9Xs0MfSJKys7MVFBTk5YLcV5vv7wZ3FxgAAMCdIgABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADDIQABAADD8YkAlJ6erg4dOigwMFCxsbHav39/tX3ff/99Pfzww2rRooVatGih+Pj4Sv3Hjx8vk8nksgwePLiuDwMAADQQXg9A69atk9Vq1dy5c3Xo0CFFR0crISFB586dq7L/zp07NWbMGP3lL39RXl6eIiIiNGjQIJ0+fdql3+DBg3X27Fnn8tFHH9XH4QAAgAbA6wFo0aJFmjRpkiZMmKCuXbsqIyNDTZo00cqVK6vs/+GHH+p3v/udYmJi1KVLFy1fvlwVFRXKzc116Wc2mxUaGupcWrRoUR+HAwAAGgCvBqCysjIdPHhQ8fHxzjY/Pz/Fx8crLy+vRmNcuXJF169fV8uWLV3ad+7cqTZt2qhz58767W9/q4sXL1Y7Rmlpqex2u8sCAADuXl4NQBcuXFB5eblCQkJc2kNCQmSz2Wo0xqxZsxQeHu4SogYPHqzVq1crNzdX8+fP165du5SYmKjy8vIqx0hNTZXFYnEuERER7h8UAADweY28XcCdePPNN7V27Vrt3LlTgYGBzvbRo0c7f+7evbuioqJ0//33a+fOnXr00UcrjZOcnCyr1epct9vthCAAAO5iXj0D1KpVK/n7+6uwsNClvbCwUKGhobfc96233tKbb76pzz//XFFRUbfse99996lVq1Y6duxYldvNZrOCg4NdFgAAcPfyagAKCAhQr169XCYw35zQHBcXV+1+CxYs0GuvvaacnBz17t37tp9z6tQpXbx4UWFhYR6pGwAANGxevwvMarXq/fff16pVq/Tdd9/pt7/9rUpKSjRhwgRJ0tixY5WcnOzsP3/+fM2ZM0crV65Uhw4dZLPZZLPZVFxcLEkqLi7WSy+9pL179+of//iHcnNzNWLECHXs2FEJCQleOUYAAOBbvD4HaNSoUTp//rxSUlJks9kUExOjnJwc58ToEydOyM/v/3LasmXLVFZWpl/96lcu48ydO1fz5s2Tv7+/vvrqK61atUqXLl1SeHi4Bg0apNdee01ms7lejw0AAPgmk8PhcHi7CF9jt9tlsVhUVFTUYOcDXb16VYmJiZKkyz2fkfwbe7kiAIBPKr+uZoc+kCRlZ2crKCjIywW5rzbf316/BAYAAFDfCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwCEAAAMBwfCIApaenq0OHDgoMDFRsbKz2799/y/4bNmxQly5dFBgYqO7du2vbtm0u2x0Oh1JSUhQWFqagoCDFx8fr6NGjdXkIAACgAfF6AFq3bp2sVqvmzp2rQ4cOKTo6WgkJCTp37lyV/b/88kuNGTNGEydO1OHDh5WUlKSkpCR98803zj4LFizQ0qVLlZGRoX379qlp06ZKSEjQtWvX6uuwAACADzM5HA6HNwuIjY3VQw89pHfeeUeSVFFRoYiICP3+97/X7NmzK/UfNWqUSkpKtGXLFmdb3759FRMTo4yMDDkcDoWHh2v69OmaMWOGJKmoqEghISHKzMzU6NGjb1uT3W6XxWJRUVGRgoODPXSk9evKlSsaMmSIJKm4+0g5/Py9XJGBOSRV3PB2FYDv8mskmbxdhHGZKsr1s683SJK2bdumJk2aeLki99Xm+7tRPdVUpbKyMh08eFDJycnONj8/P8XHxysvL6/KffLy8mS1Wl3aEhISlJWVJUkqKCiQzWZTfHy8c7vFYlFsbKzy8vKqDEClpaUqLS11rtvt9js5LJ/w78dz8z9sAABupbS0tEEHoNrw6iWwCxcuqLy8XCEhIS7tISEhstlsVe5js9lu2f/mr7UZMzU1VRaLxblERES4dTwAAKBh8OoZIF+RnJzsclbJbrc3+BBksVi0efNmb5cB/TQp/9/PyAFwZTabZTJxDcwXWCwWb5dQb7wagFq1aiV/f38VFha6tBcWFio0NLTKfUJDQ2/Z/+avhYWFCgsLc+kTExNT5Zhms1lms9ndw/BJfn5+atGihbfLAADAJ3n1ElhAQIB69eql3NxcZ1tFRYVyc3MVFxdX5T5xcXEu/SVp+/btzv6RkZEKDQ116WO327Vv375qxwQAAMbi9UtgVqtV48aNU+/evdWnTx+lpaWppKREEyZMkCSNHTtWbdu2VWpqqiRp6tSpeuSRR7Rw4UINHTpUa9eu1YEDB/Tee+9Jkkwmk6ZNm6bXX39dnTp1UmRkpObMmaPw8HAlJSV56zABAIAP8XoAGjVqlM6fP6+UlBTZbDbFxMQoJyfHOYn5xIkT8vP7vxNV/fr105o1a/TKK6/o5ZdfVqdOnZSVlaUHH3zQ2WfmzJkqKSnR5MmTdenSJfXv3185OTkKDAys9+MDAAC+x+vPAfJFd8NzgAAAMJrafH97/UnQAAAA9Y0ABAAADIcABAAADIcABAAADIcABAAADIcABAAADIcABAAADIcABAAADIcABAAADMfrr8LwRTcfjm23271cCQAAqKmb39s1eckFAagKly9fliRFRER4uRIAAFBbly9flsViuWUf3gVWhYqKCp05c0bNmjWTyWTydjkAPMhutysiIkInT57kXX/AXcbhcOjy5csKDw93eZF6VQhAAAyFlx0DkJgEDQAADIgABAAADIcABMBQzGaz5s6dK7PZ7O1SAHgRc4AAAIDhcAYIAAAYDgEIAAAYDgEIAAAYDgEIAAAYDgEIAAAYDgEIAAAYDgEIAAAYDgEIAAAYzv8DlKSTSsOb60sAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sns.boxplot(y='Exited', data=data)\n",
        "data['Exited'].mean()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "s3Rs8baNiKiw",
        "outputId": "08f1cd05-7311-4d7f-ecf6-154fe383ab81"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0.2037"
            ]
          },
          "metadata": {},
          "execution_count": 23
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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d26WLl2a7u7usbWRkZF0d3entbX1hMe8733vy/e///2MjIyMrT3//PO59NJLTxg2AMC5p6KXpTo6OvLggw/m7/7u7/LMM8/k5ptvzuDgYNasWZMkWbVqVTo7O8f2v/nmm3Po0KHceuutef7557N169Zs2LAht9xyS6XeAgAww1T0e27a29tz4MCBrFu3Lr29vVm8eHG2b98+dpPx3r17M2fOz/qrqakpTzzxRG677bZcddVVWbBgQW699dbcfvvtlXoLAMAMU9HvuakE33MDALPPrPieGwCAs0HcAABFETcAQFHEDQBQFHEDABRF3AAARRE3AEBRxA0AUBRxAwAU5bQfv/D5z3/+tH/pH/7hH05qGACAM3Xaj19461vfOu7nAwcO5LXXXsvFF1+cJHn11VdzwQUXZP78+XnhhRemfNCp4vELADD7nJXHL7z44otj2z333JPFixfnmWeeyaFDh3Lo0KE888wzefe735277777jN8AAMBkTerBmZdffnkee+yxLFmyZNz6rl278vGPfzwvvvjilA041Zy5AYDZ56w/OPOHP/xhjh07dtz68PBw+vr6JvMrAQCmxKTi5kMf+lD+4A/+ILt37x5b27VrV26++ea0tbVN2XAAABM1qbh5+OGH09jYmGXLlqWmpiY1NTVZvnx5Ghoa8tBDD031jAAAp+20/xT8573lLW/Jtm3b8vzzz+fZZ59NklxxxRV5+9vfPqXDAQBM1KTi5nXNzc0ZHR3N5ZdfnvPOO6NfBQAwJSZ1Weq1117LDTfckAsuuCDvete7snfv3iTJ2rVrc++9907pgAAAEzGpuOns7Mx//Md/ZMeOHamtrR1bb2try5YtW6ZsOACAiZrUtaTHH388W7ZsyXve855UVVWNrb/rXe/KD37wgykbDgBgoiZ15ubAgQOZP3/+ceuDg4PjYgcAYLpNKm6WLVuWrVu3jv38etA89NBDaW1tnZrJAAAmYVKXpTZs2JCPfOQj+d73vpdjx47lr//6r/O9730vTz31VP71X/91qmcEADhtkzpz8/73vz979uzJsWPHsnDhwnz961/P/Pnz09PTk6VLl071jAAAp21SD86czTw4EwBmn7P+4Mzq6urs37//uPX/+Z//SXV19WR+JQDAlJhU3JzsZM/Q0FDmzp17RgMBAJyJCd1Q/PnPfz7JT/866qGHHsqFF1449m/Dw8P55je/mSuuuGJqJwQAmIAJxc1f/dVfJfnpmZvNmzePuwQ1d+7cNDc3Z/PmzVM7IQDABEwobl588cUkyTXXXJOvfOUrueSSS87KUAAAkzWp77n5xje+MdVzAABMidOOm46Ojtx9991585vfnI6OjlPue//995/xYAAAk3HacfP000/nJz/5ydh/n4xnSwEAleRL/ACAGe+sf4nfgQMHTvpv3/nOdybzKwEApsSk4mbhwoXjngr+us997nNZvnz5GQ8FADBZk4qbjo6O/NZv/VZuvvnm/PjHP87LL7+cD33oQ/nsZz+bRx55ZKpnBAA4bZO+5+bpp5/O9ddfn6GhoRw6dCgtLS15+OGH09jYONUzTin33ADA7HPW77lJkre97W258sor89JLL2VgYCDt7e0zPmwAgPJNKm6+9a1v5aqrrsp//dd/5T//8z/zxS9+MWvXrk17e3t+9KMfTfWMAACnbVJx8+u//utpb2/Pv//7v+cd73hHbrzxxjz99NPZu3dvFi5cONUzAgCctkk9fuHrX/96PvjBD45bu/zyy/Otb30r99xzz5QMBgAwGRM6c/PRj340/f39Y2Fz77335tVXXx379x/96Ef5+7//+ykdEABgIiYUN0888USGhobGft6wYUMOHTo09vOxY8fy3HPPTd10AAATNKG4+f9/NX6OPbkBAJgFJv2n4AAAM9GE4qaqquq4p357CjgAMJNM6K+lRkdH83u/93upqalJkhw5ciQ33XRT3vzmNyfJuPtxAAAqYUJxs3r16nE//+7v/u5x+6xaterMJgIAOAMTipu/+Zu/OVtzAABMCTcUAwBFETcAQFHEDQBQFHEDABRF3AAARZkRcbNp06Y0NzentrY2LS0t2blz52kd9+ijj6aqqirXXnvt2R0QAJg1Kh43W7ZsSUdHR9avX5/du3dn0aJFWbFiRfbv33/K41566aX88R//cT7wgQ9M06QAwGxQ8bi5//7788lPfjJr1qzJO9/5zmzevDkXXHBBHn744ZMeMzw8nN/5nd/JZz7zmfzyL//yNE4LAMx0FY2bo0ePZteuXWlraxtbmzNnTtra2tLT03PS4/7sz/4s8+fPzw033PCGrzE0NJSBgYFxGwBQrorGzcGDBzM8PJyGhoZx6w0NDent7T3hMf/2b/+WL3/5y3nwwQdP6zW6urpSX18/tjU1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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df1=data[data['Exited']<1.0]\n",
        "sns.boxplot(y='Exited', data=df1)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 428
        },
        "id": "tS-VdD_GiUkk",
        "outputId": "566d41be-b67f-4b5f-d395-be954d594c74"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='Exited'>"
            ]
          },
          "metadata": {},
          "execution_count": 24
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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tuWwww7LmDFj8j//8z8DvtEDWVdXVxoaGtLZ2Zn6+vrB3g4A0Ad9ff/u88dwL7zwQuVx7bXXZvLkyXn22WezdevWbN26Nc8++2xOOeWUXHPNNQNyAAAAB4I+n1n6Tccdd1zuv//+/OEf/mGv8ba2tpx99tl54YUXBmyD1cCZJQCoPgN+Zuk3/e///m/efPPNd4zv2rUrHR0d/fmVAAAHpH7F0owZM/JXf/VXWbt2bWWsra0tF1xwQVpaWgZscwAAg61fsXTHHXeksbExU6dOTV1dXerq6jJt2rSMHTs2t99++0DvEQBg0PT51gG/afTo0XnwwQfz3//933nuueeSJBMmTMjv//7vD+jmAAAGW79i6W3jx49PT09PjjvuuAwd+p5+FQDAAalfH8O9/vrrWbhwYQ477LCceOKJ2bBhQ5Jk0aJFue666wZ0gwAAg6lfsbRkyZI89dRT+c///M8MHz68Mt7S0pKVK1cO2OYAAAZbvz47W7VqVVauXJlTTz01NTU1lfETTzwxP//5zwdscwAAg61fZ5a2bNmSMWPGvGN8+/btveIJAKDa9SuWpk6dmu985zuVn98OpNtvvz3Nzc0Ds7O9uOWWWzJ+/PgMHz4806dPz+OPP16cf99992XChAkZPnx4Jk2alAcffLDX8z09PbnqqqvyoQ99KIceemhaWlry/PPP789DAACqSL9i6Stf+UquuOKKXHDBBXnzzTdz00035eMf/3i++c1v5tprrx3oPVasXLkyixcvztVXX521a9fm5JNPzsyZM7N58+Y9zn/00Uczd+7cLFy4MOvWrcusWbMya9asPP3005U5X/3qV7Ns2bIsX748jz32WA4//PDMnDkzO3bs2G/HAQBUj379bbgk+fnPf57rrrsuTz31VF577bWccsopueyyyzJp0qSB3mPF9OnT87GPfSw333xzkmT37t1pamrKokWLcvnll79j/pw5c7J9+/Y88MADlbFTTz01kydPzvLly9PT05Nx48blkksuyV//9V8nSTo7OzN27Njceeed+fSnP92nfVX734br6enJjh07BOIBYPfu3enq6hrsbcABrb6+PrW1/fp/fQbQ8OHDM3z48Kq+/Kav79/9vjnScccdl3/6p3/q7/J99sYbb6StrS1LliypjNXW1qalpSWtra17XNPa2prFixf3Gps5c2ZWrVqVJHnh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fT8YAKCqDGosXX755ampqSk+nnvuufdlL08//XT+7M/+LFdffXU+/vGPF+cuWbIknZ2dlcfGjRvflz0CAO+/oYP54pdccknOO++84pyPfOQjaWxszObNm3uNv/nmm9m6dWsaGxv3uK6xsTFvvPFGtm3b1uvsUkdHxzvW/OxnP8uMGTNy/vnn58orr3zXfdfV1aWuru5d5wEA1W9QY2n06NEZPXr0u85rbm7Otm3b0tbWlilTpiRJHn744ezevTvTp0/f45opU6bkkEMOyZo1azJ79uwkyfr167Nhw4Y0NzdX5j3zzDM544wzMn/+/Fx77bUDcFQAwMGkKr4NlySf/OQn09HRkeXLl2fnzp1ZsGBBpk6dmhUrViRJXnrppcyYMSN33XVXpk2bliS54IIL8uCDD+bOO+9MfX19Fi1alOSta5OStz56O+OMMzJz5sx87Wtfq7zWkCFD+hRxb/NtOACoPn19/x7UM0v74p577slFF12UGTNmpLa2NrNnz86yZcsqz+/cuTPr16/P66+/Xhm74YYbKnO7u7szc+bMfOMb36g8f//992fLli25++67c/fdd1fGf/d3fze/+MUv3pfjAgAObFVzZulA5swSAFSfg+o+SwAAg0UsAQAUiCUAgAKxBABQIJYAAArEEgBAgVgCACgQSwAABWIJAKBALAEAFIglAIACsQQAUCCWAAAKxBIAQIFYAgAoEEsAAAViCQCgQCwBABSIJQCAArEEAFAglgAACsQSAECBWAIAKBBLAAAFYgkAoEAsAQAUiCUAgAKxBABQIJYAAArEEgBAgVgCACgQSwAABWIJAKBALAEAFIglAIACsQQAUCCWAAAKxBIAQIFYAgAoEEsAAAViCQCgQCwBABSIJQCAArEEAFAglgAACsQSAECBWAIAKBBLAAAFYgkAoEAsAQAUiCUAgAKxBABQIJYAAArEEgBAgVgCACgQSwAABVUTS1u3bs0555yT+vr6jBgxIgsXLsxrr71WXLNjx45ceOGFGTVqVI444ojMnj07HR0de5z7q1/9Kh/+8IdTU1OTbdu27YcjAACqUdXE0jnnnJNnnnkmDz30UB544IE88sgjOf/884trvvjFL+bb3/527rvvvvzgBz/Ipk2b8qlPfWqPcxcuXJiPfvSj+2PrAEAVq+np6ekZ7E28m2effTYnnHBCnnjiiUydOjVJsnr16px55pn55S9/mXHjxr1jTWdnZ0aPHp0VK1bk7LPPTpI899xzmThxYlpbW3PqqadW5t56661ZuXJlrrrqqsyYMSOvvPJKRowY0ef9dXV1paGhIZ2dnamvr39vBwsAvC/6+v5dFWeWWltbM2LEiEooJUlLS0tqa2vz2GOP7XFNW1tbdu7cmZaWlsrYhAkTcswxx6S1tbUy9rOf/Sx/93d/l7vuuiu1tX37z9Hd3Z2urq5eDwDg4FQVsdTe3p4xY8b0Ghs6dGhGjhyZ9vb2va4ZNmzYO84QjR07trKmu7s7c+fOzde+9rUcc8wxfd7P0qVL09DQUHk0NTXt2wEBAFVjUGPp8ssvT01NTfHx3HPP7bfXX7JkSSZOnJjPfOYz+7yus7Oz8ti4ceN+2iEAMNiGDuaLX3LJJTnvvPOKcz7ykY+ksbExmzdv7jX+5ptvZuvWrWlsbNzjusbGxrzxxhvZtm1br7NLHR0dlTUPP/xwfvrTn+b+++9Pkrx9+dZRRx2VL33pS/nbv/3bPf7uurq61NXV9eUQAYAqN6ixNHr06IwePfpd5zU3N2fbtm1pa2vLlClTkrwVOrt378706dP3uGbKlCk55JBDsmbNmsyePTtJsn79+mzYsCHNzc1Jkn/5l3/Jr3/968qaJ554In/xF3+RH/7whznuuOPe6+EBAAeBQY2lvpo4cWI+8YlP5LOf/WyWL1+enTt35qKLLsqnP/3pyjfhXnrppcyYMSN33XVXpk2bloaGhixcuDCLFy/OyJEjU19fn0WLFqW5ubnyTbjfDqKXX3658nr78m04AODgVRWxlCT33HNPLrroosyYMSO1tbWZPXt2li1bVnl+586dWb9+fV5//fXK2A033FCZ293dnZkzZ+Yb3/jGYGwfAKhSVXGfpQOd+ywBQPU5qO6zBAAwWMQSAECBWAIAKBBLAAAFYgkAoEAsAQAUiCUAgAKxBABQIJYAAArEEgBAgVgCACgQSwAABWIJAKBALAEAFIglAIACsQQAUCCWAAAKxBIAQIFYAgAoEEsAAAViCQCgQCwBABSIJQCAArEEAFAglgAACsQSAECBWAIAKBBLAAAFYgkAoEAsAQAUiCUAgAKxBABQIJYAAArEEgBAgVgCACgQSwAABWIJAKBALAEAFIglAIACsQQAUCCWAAAKxBIAQMHQwd7AwaCnpydJ0tXVNcg7AQD66u337bffx/dGLA2AV199NUnS1NQ0yDsBAPbVq6++moaGhr0+X9PzbjnFu9q9e3c2bdqUI488MjU1NYO9HWAAdXV1pampKRs3bkx9ff1gbwcYQD09PXn11Vczbty41Nbu/coksQRQ0NXVlYaGhnR2dool+IBygTcAQIFYAgAoEEsABXV1dbn66qtTV1c32FsBBolrlgAACpxZAgAoEEsAAAViCQCgQCwBABSIJQCAArEEAFAglgAACsQSAEDB/wMQfcn1oe+9CgAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df1.boxplot()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 447
        },
        "id": "w0umDBXmia6W",
        "outputId": "bdde6670-d92e-4bc9-f40b-0385abd20ec1"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 32
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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+iE7OxthYWH4+OOPlfEWFhbYuHEjRo4ciaCgINja2iI8PBxTp05V2nh7e2PTpk14/fXXsWDBAtSpUwefffYZwsLCqmKWiIiI6BFTKSFn9+7dZo+trKywePFiLF68+L7TeHl5YfPmzSX2GxwcjKNHj5ZHiURERKQyVXImh4joYST/lYWs7LwHNwSQ9GeW8q/pQsyS2Bos4V3T9m/VR0SPFoYcIqoWkv/KQufZu8s83djvEkrddtd/gxl0iFSEIYeIqgXTGZz5AwLh4/LgbzjLup2Njbtj0Cs4CLbWRb86orDzlzMxek18qc8SEVH1wJBDRNWKj4sdmtR2eGC73NxcpNUCWng5PhLfFUJEla9Cf4WciIiIqKow5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqMeQQERGRKjHkEBERkSox5BAREZEqWVZ1AdXF7dx8AMCJSzce2DbrdjYO/wm4/XYNttaGEtuev5xZLvURERGROYacUkr6vzDy5rqEUk5hiS/PHyp1/7YGvhRERP8kfPNc8XhkLaXQxm4AgAYudrDWWZTYNjH1BsZ+l4A5TzeFr7vDA/u2NVjCu6ZtudRJRETVA988VzwugVJystVj4ON1S9U2Ly8PANCgli2a1H5wyCEion8evnmueAw5REREVYBvnise764iIiIiVWLIISIiIlViyCEiIiJVYsghIiIiVWLIISIiIlViyCEiIiJVYsghIiIiVWLIISIiIlViyCEiIiJVKveQM336dLRu3Rr29vZwcXFB3759kZiYaNbmzp07iIiIgLOzM+zs7NCvXz+kp6ebtbl48SJ69uwJGxsbuLi4YNy4cco3Pprs3r0bLVq0gMFggI+PD1auXFnes0NERETVVLmHnF9++QURERE4cOAAoqKikJubi9DQUGRlZSltXn/9dfz0009Yu3YtfvnlF6SkpODf//63Mj4/Px89e/ZETk4O9u/fj//9739YuXIlJk2apLRJTk5Gz5490blzZ8THx2P06NEYOnQofv755/KeJSIiIqqGyv23q7Zu3Wr2eOXKlXBxcUFcXBw6deqEGzdu4PPPP8fq1avx5JNPAgBWrFgBf39/HDhwAG3btsW2bdtw6tQpbN++Ha6urggMDMS0adPwxhtvYPLkydDr9ViyZAm8vb0xZ84cAIC/vz/27duHefPmISwsrLxni4iIiKqZCv+Bzhs3bgAAnJycAABxcXHIzc1FSEiI0sbPzw9169ZFTEwM2rZti5iYGDRt2hSurq5Km7CwMIwcORInT55E8+bNERMTY9aHqc3o0aPvW0t2djays7OVxxkZGQCA3Nxc5Obm/u15NTF9rJaXl1eu/VYkU53VpV6ANVemR6Husm5XZan5UdlmH4XlXFasuXI8KutoWVTkci5tnxUacgoKCjB69Gi0b98eTZo0AQCkpaVBr9ejRo0aZm1dXV2RlpamtCkccEzjTeNKapORkYHbt2/D2tq6SD3Tp0/HlClTigzftm0bbGxsHm4mi/F7JgBY4sCBA7h0oty6rRRRUVFVXUKZsebKU5V1m7arffv24Te70k9Xmpoftu+KUh3XD9ZcsXhcMXfr1q1StavQkBMREYETJ05g3759Ffk0pTZhwgSMGTNGeZyRkQFPT0+EhobCaDSW2/Mcu3gVSDiMtm3bIqCuU7n1W5Fyc3MRFRWFrl27QqfTVXU5pcKaK8+jUPfJlAzMTjiADh06oLHHg7fXstRc1r4ryqOwnMuKNVcOHlfMmT6JeZAKCzmRkZHYuHEj9uzZgzp16ijD3dzckJOTg+vXr5udzUlPT4ebm5vS5uDBg2b9me6+Ktzm3juy0tPTYTQaiz2LAwAGgwEGg6HIcJ1OV64vgKWlpfJvddmATMp7WVQG1lx5qrLuh92uSlPzo7bNVsf1gzVXrEdtHS2LiljOpe2v3O+uEhFERkZi/fr12LlzJ7y9vc3Gt2zZEjqdDjt27FCGJSYm4uLFiwgKCgIABAUFISEhAZcvX1baREVFwWg0olGjRkqbwn2Y2pj6ICIion+2cj+TExERgdWrV+OHH36Avb29cg2Ng4MDrK2t4eDggCFDhmDMmDFwcnKC0WjEq6++iqCgILRt2xYAEBoaikaNGuH555/HzJkzkZaWhokTJyIiIkI5EzNixAh89NFHGD9+PF566SXs3LkT3377LTZt2lTes0RERETVULmfyfnkk09w48YNBAcHw93dXflbs2aN0mbevHno1asX+vXrh06dOsHNzQ3r1q1TxltYWGDjxo2wsLBAUFAQnnvuOQwePBhTp05V2nh7e2PTpk2IiopCQEAA5syZg88++4y3jxMRERGACjiTIyIPbGNlZYXFixdj8eLF923j5eWFzZs3l9hPcHAwjh49WuYaiYiISP3421VERESkSgw5REREpEoMOURERKRKDDlERESkSgw5REREpEoMOURERKRKDDlERESkSgw5REREpEoMOURERKRKDDlERESkSgw5REREpEoMOURERKRKDDlERESkSgw5REREpEoMOURERKRKDDlERESkSgw5REREpEoMOURERKRKDDlERESkSgw5REREpEoMOURERKRKDDlERESkSgw5REREpEqWVV0AEVFpZOffgdbqEpIzEqG1sntg+7y8PKTkpeD01dOwtCx5V5eckQmt1SVk598B4FBOFRNRVWPIIaJqISXrN9h6L8JbB8s23cdbPy5VO1tvICUrEC3h+hDVEdGjiCGHiKoFD1svZCW/igUDAtHApXRncqL3RaN9h/YPPJOTdDkTo9bEw6OzV3mVS0SPAIYcIqoWDBZWKLhTG95GXzRyfvBHSrm5uUi2TIa/kz90Ol2JbQvu3EDBnT9hsLAqr3KJ6BHAC4+JiIhIlRhyiIiISJUYcoiIiEiVGHKIiIhIlRhyiIiISJUYcoiIiEiVGHKIiIhIlRhyiIiISJUYcoiIiEiVGHKIiIhIlRhyiIiISJUYcoiIiEiVGHKIiIhIlRhyiIiISJUYcoiIiEiVGHKIiIhIlRhyiIiISJUsq7oAqny3bt3CmTNnzIZl3s7G/oQkONY8DDtrQ5Fp/Pz8YGNjU1klEhER/W0MOf9AZ86cQcuWLYsdN/M+08TFxaFFixYVVxQREVE5Y8j5B/Lz80NcXJzZsMTU6xizNgFz+zeFr3uNYqchIiKqThhy/oFsbGyKnJXR/nYFhr234d8kAIFezlVUGRERUflhyFG55L+ykJWd98B2SX9mKf9aWpZutbA1WMK7pu3fqo+IiKiiMOSoWPJfWeg8e3eZphn7XUKZ2u/6bzCDDhERPZIYclTMdAZn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0qVLFwEgGRkZZiGnTp06snr1annrrbfE3t5e7Ozs5MqVK0rdBoNBunbtKu+8844AkCZNmsjo0aPl7Nmz8vTTTwsAWbp0qVy4cEFeeOEFASDz58+Xe2VnZyvrV15enqSmporRaJT58+dLamqq3Lp1q9h905EjRwSA/Pjjj/ddv+fOnSs6nU5atWpVZN9j2g84OztL3759ZezYsbJgwQLx9PQUAMp2sGLFCrG3txdLS0uZO3euJCcny/z58wWA3Lx5U/Lz88XOzk40Go0EBATIk08+KVFRUaLVamXu3Lly9OhRcXV1lV69eomHh4fY29vL7NmzJSAgQHQ6nYwdO1bZvrdu3arM39GjR8VgMMjIkSMlPj5eduzYIX379pWdO3dKfHy81KtXTzQajWzevFlSU1MlLy9Pee1effVVOXPmjISFhclTTz2lvHE6c+aMtG7dWgk53bp1M1vfTp06Jc8++6x4eHiI0WiUzZs3y+jRo6Vhw4YycuRI8fHxkStXrkidOnWkRYsWMnToUBk6dKhZyDFtP//5z3/E1tZWgoKCxMHBQUaNGiV6vV46deokAMTb21vGjBmjHMxbtmwpwcHB8tprr8mnn34qXl5e0rt3b/H19ZWRI0dKeHi42NraSvPmzcXOzk6+/PJLcXZ2lv/+97/Kdl+3bl2pW7euLF++XN58802xtLQUnU4nu3fvlgMHDiiB09Sn0WgUo9GoLPOwsDDp1KmT2Zvpe3333Xfy/fffy7lz56R3797i6uoqTZs2VbbHwuvquHHjxMvLS8aPHy9fffWV6PV6ef3118XGxkbWrFljFnJsbW3FxsZGIiMjZffu3RIXFydarVbWrVsntra2Mm/ePNmwYYOyvF544QWlpu7du0tAQIDExMTI4cOHpV27dmJtbf3PCjmxsbECQNatW3ffNqUJOb1795YXX3yx1NOLiHh4eMj7779vNqx169byyiuvmE332WefKeO//vprJc2aap4+fbr4+voqbRo0aCCrV68WADJ69GgRubvDDwoKki5dusi4cePMdqxffvmluLu7Kzs3S0tLuXTpkjzzzDPSo0cP2bJlixIMBgwYYBZyRP7/O79r166Zzct3330njo6OYmVlJe3atZMJEybIl19+qdT+888/i1arlcTERHF2dhZbW1uxtbWV8ePHy969e0Wn00mXLl3M+qxRo4a4u7uL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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data[\"CustomerId\"].unique()"
      ],
      "metadata": {
        "id": "ts9jJNW3iqHu",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1cf9a129-fed7-497d-e75d-28b29589fc0e"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "array([2736, 3258, 2104, ...,  717, 4656, 2497])"
            ]
          },
          "metadata": {},
          "execution_count": 26
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.feature_selection import chi2\n",
        "X=data.drop(columns=['CreditScore'])\n",
        "Y=data['CreditScore']"
      ],
      "metadata": {
        "id": "F77k55vkTv0P"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chi_scores=chi2(X,Y)"
      ],
      "metadata": {
        "id": "UhP2NA_idn5g"
      },
      "execution_count": 35,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "chi_scores\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Lf0DN2ZzeOLf",
        "outputId": "59421726-fbb6-4924-c8d0-ea0229bb77a9"
      },
      "execution_count": 36,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "(array([7.59443198e+05, 4.59606491e+02, 2.12464638e+02, 7.26390408e+02,\n",
              "        9.89317236e+05, 2.74967116e+02, 1.20496837e+02, 2.15945775e+02,\n",
              "        8.13682083e+05, 4.06285346e+02]),\n",
              " array([0.00000000e+00, 4.83244757e-01, 1.00000000e+00, 2.16767076e-14,\n",
              "        0.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00,\n",
              "        0.00000000e+00, 9.63198761e-01]))"
            ]
          },
          "metadata": {},
          "execution_count": 36
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "chi_values=pd.Series(chi_scores[0],index=X.columns)\n",
        "chi_values.sort_values(ascending=False,inplace=True)\n",
        "chi_values.plot.bar()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 562
        },
        "id": "iJvr00MPeQVS",
        "outputId": "45152f81-1200-4f6a-fe62-2c6cad5f65b1"
      },
      "execution_count": 37,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: >"
            ]
          },
          "metadata": {},
          "execution_count": 37
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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ywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJZSw7AD2b87htr/17XJre+bV/DyIioqK80JmRhQsXwtnZGWZmZmjatCliY2OfuX9oaCjq1KkDc3NzODk5YdSoUXjw4MELBSYiIqKSRecysm7dOvj7+2PixIk4duwYGjZsCB8fH9y8ebPQ/VevXo1x48Zh4sSJOH36NH766SesW7cOX3/99UuHJyIiIuXTuYyEhIRgyJAh8PX1haurK8LCwlC6dGksWbKk0P0PHjyI5s2bo2/fvnB2dsa7776Ljz766LlnU4iIiMgw6FRGcnJycPToUXh7e//vD1Cr4e3tjZiYmEJf8/bbb+Po0aOa8nHx4kVs374dnTp1KvL7ZGdnIz09XetBREREJZNOA1hv376NvLw82Nvba223t7fHmTNnCn1N3759cfv2bbRo0QJCCOTm5mLo0KHPvEwTHByMSZMm6RKNiIiIFOq139q7Z88eTJs2Dd9//z2OHTuGTZs2Ydu2bZgyZUqRrwkMDERaWprmceXKldcdk4iIiCTR6cyInZ0djIyMkJKSorU9JSUFDg4Ohb5mwoQJ+OSTTzB48GAAgJubGzIzM/HZZ5/hm2++gVpdsA+ZmprC1NRUl2hERESkUDqdGTExMUHjxo0RFRWl2Zafn4+oqCh4eXkV+pqsrKwChcPIyAgAIITQNS8RERGVMDpPeubv748BAwbA09MTTZo0QWhoKDIzM+Hr6wsA6N+/PxwdHREcHAwA6Nq1K0JCQuDh4YGmTZvi/PnzmDBhArp27aopJURERGS4dC4jvXv3xq1btxAUFITk5GS4u7sjIiJCM6g1KSlJ60zI+PHjoVKpMH78eFy7dg3ly5dH165dMXXq1Fd3FERERKRYKqGAayXp6emwsrJCWloaLC0ti/WakjKNekk5DiIiMjzFff/mQnlEREQkFcsIERERScUyQkRERFKxjBAREZFULCNEREQkFcsIERERScUyQkRERFLpPOkZka44VwoRET0Lz4wQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSsYwQERGRVCwjREREJBXLCBEREUnFMkJERERSvVAZWbhwIZydnWFmZoamTZsiNjb2mfvfvXsXw4YNQ8WKFWFqaoratWtj+/btLxSYiIiIShZjXV+wbt06+Pv7IywsDE2bNkVoaCh8fHxw9uxZVKhQocD+OTk5aN++PSpUqICNGzfC0dERly9fhrW19avIT0RERAqncxkJCQnBkCFD4OvrCwAICwvDtm3bsGTJEowbN67A/kuWLEFqaioOHjyIUqVKAQCcnZ1fLjURERGVGDpdpsnJycHRo0fh7e39vz9ArYa3tzdiYmIKfc2vv/4KLy8vDBs2DPb29qhfvz6mTZuGvLy8Ir9PdnY20tPTtR5ERERUMulURm7fvo28vDzY29trbbe3t0dycnKhr7l48SI2btyIvLw8bN++HRMmTMDs2bPx3XffFfl9goODYWVlpXk4OTnpEpOIiIgU5LXfTZOfn48KFSrgxx9/ROPGjdG7d2988803CAsLK/I1gYGBSEtL0zyuXLnyumMSERGRJDqNGbGzs4ORkRFSUlK0tqekpMDBwaHQ11SsWBGlSpWCkZGRZpuLiwuSk5ORk5MDExOTAq8xNTWFqampLtGIiIhIoXQ6M2JiYoLGjRsjKipKsy0/Px9RUVHw8vIq9DXNmzfH+fPnkZ+fr9mWkJCAihUrFlpEiIiIyLDo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Cw4OhpWVlebh5OSkS0wiIiJSkDd6N8306dOxdu1abN68GWZmZkXuFxgYiLS0NM3jypUrbzAlERERvUnGuuxsZ2cHIyMjpKSkaG1PSUmBg4PDM187a9YsTJ8+Hbt27UKDBg2eua+pqSlMTU11iUZEREQKpdOZERMTEzRu3Fhr8OnjwaheXl5Fvm7mzJmYMmUKIiIi4Onp+eJpiYiIqMTR6cwIAPj7+2PAgAHw9PREkyZNEBoaiszMTPj6+gIA+vfvD0dHRwQHBwMAZsyYgaCgIKxevRrOzs6asSVly5ZF2bJlX+GhEBERkRLpXEZ69+6NW7duISgoCMnJyXB3d0dERIRmUGtSUhLU6v+dcFm0aBFycnLwwQcfaP05EydOxLfffvty6YmIiEjxdC4jADB8+HAMHz680Of27Nmj9fWlS5de5FsQERGRgeDaNERERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQsI0RERCQVywgRERFJxTJCREREUrGMEBERkVQvVEYWLlwIZ2dnmJmZoWnTpoiNjX3m/hs2bEDdunVhZmYGNzc3bN++/YXCEhERUcmjcxlZt24d/P39MXHiRBw7dgwNGzaEj48Pbt68Wej+Bw8exEcffYRPP/0Ux48fR/fu3dG9e3f8/fffLx2eiIiIlE/nMhISEoIhQ4bA19cXrq6uCAsLQ+nSpbFkyZJC9587dy46dOiA0aNHw8XFBVOmTEGjRo2w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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "balance, estimatedsalary, customerid"
      ],
      "metadata": {
        "id": "vBOcKThGebUe"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "iJ1iOAfBeTgO"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}