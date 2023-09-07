using Microsoft.Maui.Controls;
using FirebaseAdmin.Auth;
using Firebase.Database;
using Firebase.Database.Query;
using MauiTestApp.Features;
using Firebase.Auth;

namespace MauiTestApp
{
    public partial class LoginPage : ContentPage
    {
        public string email;
        public string password;

        public LoginPage()
        {
            InitializeComponent();
        }

        private void EmailInputTextChanged(object sender, TextChangedEventArgs e)
        {
            email = e.NewTextValue;
        }
        private void PasswordInputTextChanged(object sender, TextChangedEventArgs e)
        {
            password = e.NewTextValue;
        }

        private async void LoginUserClicked(object sender, EventArgs e)
        {
            var app = Application.Current as App;

            var errorResult = "Application is null";

            if (app != null)
            {
                try
                {
                    var userCredential = await app.authClient.SignInWithEmailAndPasswordAsync(email, password);
                    List<string> products = new List<string>();

                    var firebaseUser = new FirebaseUser
                    {
                        FirebaseUserEmail = email,
                        FirebaseUserProducts = new List<string>()
                    };

                    if (userCredential != null)
                    {
                        firebaseUser = await app.firebaseClient.Child("users").Child(userCredential.User.Uid).OnceSingleAsync<FirebaseUser>();

                        await Navigation.PushAsync(new ProductMenu(userCredential.User.Uid, firebaseUser.FirebaseUserEmail, firebaseUser.FirebaseUserProducts));
                    }
                }
                catch (Exception ex)
                {
                    // Handle the exception here
                    errorResult = "Error: " + ex.Message;
                    await DisplayAlert("Alert", errorResult, "OK");
                }
            }
            else
            {
                // Handle the case where the app is null
                await DisplayAlert("Alert", errorResult, "OK");
            }
        }
    }
}