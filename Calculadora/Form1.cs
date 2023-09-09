using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Globalization;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Calculadora
{
    public partial class Form1 : Form
    {
        decimal valor1 = 0, valor2 = 0;
        string ope = "";
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void button18_Click(object sender, EventArgs e)
        {
            label1.Text = label1.Text + "0";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            label1.Text += "1";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            label1.Text += "2";
        }

        private void button15_Click(object sender, EventArgs e)
        {
            label1.Text += "3";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            label1.Text += "4";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            label1.Text += "5";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            label1.Text += "6";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            label1.Text += "7";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            label1.Text += "8";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            label1.Text += "9";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            valor1=decimal.Parse(label1.Text,CultureInfo.InvariantCulture);
            //CultureInfo.InvariantCulture utilizado para converter
            //ex: label1=2.5 com conversao fica label1=2.5 sem conversao fica label1=25
            label1.Text = "";
            ope = "multiplicar";
            label2.Text = "x";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            valor2 = decimal.Parse(label1.Text, CultureInfo.InvariantCulture);

            if (ope == "multiplicar")
            {
                label1.Text =Convert.ToString( valor1 * valor2);
                ope = "";
            } else if (ope == "dividir")
            {
                label1.Text = Convert.ToString(valor1 / valor2);
                ope = "";
            }
            else if(ope == "subtrair")
            {
                label1.Text = Convert.ToString(valor1 - valor2);
                ope = "";
            }
            else if(ope == "somar")
            {
                label1.Text = Convert.ToString(valor1 + valor2);
                ope = "";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text = "";
            valor1 = 0;
            valor2 = 0;
            label2.Text = "";
            ope = "";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            valor1 = decimal.Parse(label1.Text, CultureInfo.InvariantCulture);
            //CultureInfo.InvariantCulture utilizado para converter
            //ex: label1=2.5 com conversao fica label1=2.5 sem conversao fica label1=25
            label1.Text = "";
            ope = "dividir";
            label2.Text = "/";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            valor1 = decimal.Parse(label1.Text, CultureInfo.InvariantCulture);
            //CultureInfo.InvariantCulture utilizado para converter
            //ex: label1=2.5 com conversao fica label1=2.5 sem conversao fica label1=25
            label1.Text = "";
            ope = "subtrair";
            label2.Text = "-";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            valor1 = decimal.Parse(label1.Text, CultureInfo.InvariantCulture);
            //CultureInfo.InvariantCulture utilizado para converter
            //ex: label1=2.5 com conversao fica label1=2.5 sem conversao fica label1=25
            label1.Text = "";
            ope = "somar";
            label2.Text = "+";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            label1.Text += ".";
        }
    }
}
