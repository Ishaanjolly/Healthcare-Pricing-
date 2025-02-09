{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "def apply_format_NEOS_sol(input_file):\n",
    "    '''\n",
    "    Takes the results extracted from NEOS and get them in a dataframe format\n",
    "    \n",
    "    Input:\n",
    "            input_file (str) : file with the results from NEOS in txt format \n",
    "    \n",
    "    Output:\n",
    "            sol : dataframe with NEOS solutions\n",
    "    '''\n",
    "\n",
    "    import numpy as np\n",
    "    import pandas as pd\n",
    "    import matplotlib.pyplot as plt\n",
    "    import seaborn as sns\n",
    "    import warnings\n",
    "    warnings.simplefilter(action='ignore', category=FutureWarning)\n",
    "\n",
    "    f = open('10000_data.txt','r');\n",
    "    Lines =f.readlines()\n",
    "\n",
    "    objective = []\n",
    "    gamma = []\n",
    "    demand = []\n",
    "    mu = []\n",
    "    p_pub_x = []\n",
    "    p_priv_x = []\n",
    "    p_pub_y = []\n",
    "    p_priv_y = []\n",
    "    q_pub_x = []\n",
    "    q_priv_x = []\n",
    "    q_pub_y = []\n",
    "    q_priv_y = []\n",
    "    z=[]\n",
    "    PubCost = []\n",
    "    K_x = []\n",
    "    K_y = []\n",
    "    P_x = []\n",
    "    P_y = []\n",
    "\n",
    "    for i in range(len(Lines)):\n",
    "        if Lines[i][0:5] == 'gamma':\n",
    "            gamma = np.append(gamma, float(Lines[i][8:]))\n",
    "            if Lines[i-1][0:9] != 'Objective':\n",
    "                objective = np.append(objective,'Not feasible')\n",
    "            else:\n",
    "                objective = np.append(objective,float(Lines[i-1][9:]))\n",
    "        elif Lines[i][0:6] == 'demand':\n",
    "            demand = np.append(demand, float(Lines[i][8:]))\n",
    "        elif Lines[i][0:2] == 'mu':\n",
    "            mu = np.append(mu, float(Lines[i][4:]))\n",
    "        elif Lines[i][0:5] == 'price':\n",
    "            p_pub_x = np.append(p_pub_x, float(Lines[i+1][10:]))\n",
    "            p_priv_x = np.append(p_priv_x, float(Lines[i+2][10:]))\n",
    "            p_pub_y = np.append(p_pub_y, float(Lines[i+3][10:]))\n",
    "            p_priv_y = np.append(p_priv_y, float(Lines[i+4][10:]))\n",
    "        elif Lines[i][0:5] == 'quant':\n",
    "            q_pub_x = np.append(q_pub_x, float(Lines[i+1][10:]))\n",
    "            q_priv_x = np.append(q_priv_x, float(Lines[i+2][10:]))\n",
    "            q_pub_y = np.append(q_pub_y, float(Lines[i+3][10:]))\n",
    "            q_priv_y = np.append(q_priv_y, float(Lines[i+4][10:]))\n",
    "        elif Lines[i][0] == 'K':\n",
    "            K_x = np.append(K_x, float(Lines[i+1][2:]))\n",
    "            K_y = np.append(K_y, float(Lines[i+2][2:]))\n",
    "        elif Lines[i][0:2] == 'P ':\n",
    "            P_x = np.append(P_x, float(Lines[i+1][2:]))\n",
    "            P_y = np.append(P_y, float(Lines[i+2][2:]))\n",
    "\n",
    "        elif Lines[i][0] == 'z':\n",
    "            z = np.append(z, float(Lines[i][4:]))\n",
    "        elif Lines[i][0:7] == 'PubCost':\n",
    "            PubCost = np.append(PubCost, float(Lines[i][10:]))\n",
    "\n",
    "    sol = pd.DataFrame()\n",
    "    sol['value_obj_func'] = objective\n",
    "    sol['gamma'] = gamma\n",
    "    sol['demand'] = demand\n",
    "    sol['mu'] = mu\n",
    "    sol['K_infanrix'] = K_x\n",
    "    sol['K_daptacel'] = K_y\n",
    "    sol['P_infanrix'] = P_x\n",
    "    sol['P_daptacel'] = P_y\n",
    "    sol['pub_p_infanrix'] = p_pub_x\n",
    "    sol['priv_p_infanrix'] = p_priv_x\n",
    "    sol['pub_p_daptacel'] = p_pub_y\n",
    "    sol['priv_p_daptacel'] = p_priv_y\n",
    "    sol['pub_q_infanrix'] = q_pub_x\n",
    "    sol['priv_q_infanrix'] = q_priv_x\n",
    "    sol['pub_q_daptacel'] = q_pub_y \n",
    "    sol['priv_q_daptacel'] = q_priv_y \n",
    "    sol['z'] = z\n",
    "    sol['PubCost'] = PubCost\n",
    "    \n",
    "    return sol\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
