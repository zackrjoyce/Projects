using Microsoft.Maui.Controls;

namespace MauiTestApp
{
    public partial class Authentication : ContentPage
    {
        public Authentication()
        {
            InitializeComponent();
        }

        private async void LoginClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new LoginPage());
        }

        private async void RegisterClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new RegisterPage());
        }
    }
}