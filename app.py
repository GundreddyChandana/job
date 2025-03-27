{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "698bc2d6-c928-4064-92c9-02bdf479afa0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "jobs_df = pd.read_csv(\"Jobs_Dataset.csv\")\n",
    "employment_df = pd.read_excel(\"employment.xlsx\")\n",
    "education_df = pd.read_csv(\"education.csv\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "6ab8c28d-83de-4a21-8bf5-384e75f5be72",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\gundr\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:3585: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, jsonify\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/recommend', methods=['POST'])\n",
    "def recommend():\n",
    "    data = request.json\n",
    "    user_skills = data.get(\"skills\", [])\n",
    "    # Implement job filtering logic here\n",
    "    recommended_jobs = jobs_df[jobs_df['skills'].str.contains('|'.join(user_skills), na=False)]\n",
    "    return jsonify(recommended_jobs.to_dict(orient='records'))\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "59b1b709-56fa-4cbe-897e-4710c3cafb2b",
   "metadata": {},
   "outputs": [
    {
     "ename": "AssertionError",
     "evalue": "View function mapping is overwriting an existing endpoint function: home",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAssertionError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[10], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mflask\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m render_template\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;129m@app\u001b[39m\u001b[38;5;241m.\u001b[39mroute(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m/\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mhome\u001b[39m():\n\u001b[0;32m      5\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m render_template(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mindex.html\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\flask\\sansio\\scaffold.py:362\u001b[0m, in \u001b[0;36mScaffold.route.<locals>.decorator\u001b[1;34m(f)\u001b[0m\n\u001b[0;32m    360\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mdecorator\u001b[39m(f: T_route) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m T_route:\n\u001b[0;32m    361\u001b[0m     endpoint \u001b[38;5;241m=\u001b[39m options\u001b[38;5;241m.\u001b[39mpop(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mendpoint\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m)\n\u001b[1;32m--> 362\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39madd_url_rule(rule, endpoint, f, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39moptions)\n\u001b[0;32m    363\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m f\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\flask\\sansio\\scaffold.py:47\u001b[0m, in \u001b[0;36msetupmethod.<locals>.wrapper_func\u001b[1;34m(self, *args, **kwargs)\u001b[0m\n\u001b[0;32m     45\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mwrapper_func\u001b[39m(\u001b[38;5;28mself\u001b[39m: Scaffold, \u001b[38;5;241m*\u001b[39margs: t\u001b[38;5;241m.\u001b[39mAny, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs: t\u001b[38;5;241m.\u001b[39mAny) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m t\u001b[38;5;241m.\u001b[39mAny:\n\u001b[0;32m     46\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_check_setup_finished(f_name)\n\u001b[1;32m---> 47\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m f(\u001b[38;5;28mself\u001b[39m, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\flask\\sansio\\app.py:657\u001b[0m, in \u001b[0;36mApp.add_url_rule\u001b[1;34m(self, rule, endpoint, view_func, provide_automatic_options, **options)\u001b[0m\n\u001b[0;32m    655\u001b[0m old_func \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mview_functions\u001b[38;5;241m.\u001b[39mget(endpoint)\n\u001b[0;32m    656\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m old_func \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;129;01mand\u001b[39;00m old_func \u001b[38;5;241m!=\u001b[39m view_func:\n\u001b[1;32m--> 657\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mAssertionError\u001b[39;00m(\n\u001b[0;32m    658\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mView function mapping is overwriting an existing\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    659\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m endpoint function: \u001b[39m\u001b[38;5;132;01m{\u001b[39;00mendpoint\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    660\u001b[0m     )\n\u001b[0;32m    661\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mview_functions[endpoint] \u001b[38;5;241m=\u001b[39m view_func\n",
      "\u001b[1;31mAssertionError\u001b[0m: View function mapping is overwriting an existing endpoint function: home"
     ]
    }
   ],
   "source": [
    "from flask import render_template\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template('index.html')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87b5af6b-fd9c-44f5-865a-ede56469595f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
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
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
