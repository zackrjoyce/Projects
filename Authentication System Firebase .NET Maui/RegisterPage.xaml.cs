using Microsoft.Maui.Controls;
using FirebaseAdmin.Auth;
using System.Diagnostics;
using Firebase.Auth;
using Firebase.Database;
using Firebase.Database.Query;
using MauiTestApp.Features;
using static Google.Apis.Auth.OAuth2.Web.AuthorizationCodeWebApp;

namespace MauiTestApp
{
    public partial class RegisterPage : ContentPage
    {
        public string email;
        public string password;

        public RegisterPage()
        {
            InitializeComponent();
        }

        private void emailInput_TextChanged(object sender, TextChangedEventArgs e)
        {
            email = e.NewTextValue;
        }
        private void passwordInput_TextChanged(object sender, TextChangedEventArgs e)
        {
            password = e.NewTextValue;
        }

        private async void RegisterUserClicked(object sender, EventArgs e)
        {
            var app = Application.Current as App;
            var errorResult = "Application is null";

            if (app != null)
            {
                try
                {
                    var userCredential = await app.authClient.CreateUserWithEmailAndPasswordAsync(email, password);
                    List<string> products = new List<string> { "SNOOZ Original" };


                    var firebaseUser = new FirebaseUser
                    {
                        FirebaseUserEmail = email,
                        FirebaseUserProducts = products
                    };

                    if (userCredential != null)
                    {
                        // Get a reference to the user's node and set the value
                        await app.firebaseClient.Child("users").Child(userCredential.User.Uid).PutAsync(firebaseUser);

                        await Navigation.PushAsync(new ProductMenu(userCredential.User.Uid, email, products));
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