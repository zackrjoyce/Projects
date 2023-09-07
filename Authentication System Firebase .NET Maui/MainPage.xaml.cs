using Microsoft.Maui.Controls;

namespace MauiTestApp
{
    public partial class MainPage : ContentPage
    {
        public MainPage()
        {
            InitializeComponent();
        }

        private async void OnGetStartedClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new Authentication());
        }
    }
}