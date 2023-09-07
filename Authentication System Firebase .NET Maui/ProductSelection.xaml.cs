using Microsoft.Maui.Controls;
using FirebaseAdmin.Auth;
using Firebase.Auth;
using Firebase.Database.Query;
using Google.Apis.Auth.OAuth2;
using MauiTestApp.Features;
using Microsoft.Maui.ApplicationModel.Communication;

namespace MauiTestApp
{
    public partial class ProductSelection : ContentPage
    {
        public string UserUid;
        public string UserEmail;
        public List<string> UserProducts;
        private ProductMenu productMenu;

        App app = Application.Current as App;

        public ProductSelection(string uid, string email, List<string> products, ProductMenu menu)
        {
            InitializeComponent();

            UserUid = uid;
            UserEmail = email;
            UserProducts = products;
            productMenu = menu;
        }

        public async void AddSnoozOriginalButtonClicked(object sender, EventArgs e)
        {
            await AddSnoozOriginalButtonClickedUpdate();
        }

        public async Task AddSnoozOriginalButtonClickedUpdate()
        {
            try
            {
                string product = "SNOOZ Original";

                UserProducts.Add(product);

                productMenu.UserProducts = UserProducts;

                Label productLabel = new Label
                {
                    Text = product,
                    HorizontalOptions = LayoutOptions.Center,
                    VerticalOptions = LayoutOptions.Center
                };

                productMenu.productsView.Children.Add(productLabel);

                var firebaseUser = new FirebaseUser
                {
                    FirebaseUserEmail = UserEmail,
                    FirebaseUserProducts = UserProducts
                };

                await app.firebaseClient.Child("users").Child(UserUid).PutAsync(firebaseUser);
                await Navigation.PopAsync();
            }
            catch (Exception ex)
            {
                // Handle exceptions
                Console.WriteLine($"Error adding Snooz Go: {ex.Message}");
            }
        }

        public async void AddSnoozGoButtonClicked(object sender, EventArgs e)
        {
            await AddSnoozGoButtonClickedUpdate();
        }

        public async Task AddSnoozGoButtonClickedUpdate()
        {
            try
            {
                string product = "SNOOZ Go";

                UserProducts.Add(product);

                productMenu.UserProducts = UserProducts;

                Label productLabel = new Label
                {
                    Text = product,
                    HorizontalOptions = LayoutOptions.Center,
                    VerticalOptions = LayoutOptions.Center
                };

                productMenu.productsView.Children.Add(productLabel);

                var firebaseUser = new FirebaseUser
                {
                    FirebaseUserEmail = UserEmail,
                    FirebaseUserProducts = UserProducts
                };

                await app.firebaseClient.Child("users").Child(UserUid).PutAsync(firebaseUser);
                await Navigation.PopAsync();
            }
            catch (Exception ex)
            {
                // Handle exceptions
                Console.WriteLine($"Error adding Snooz Go: {ex.Message}");
            }
        }

        public async void AddSnoozProButtonClicked(object sender, EventArgs e)
        {
            await AddSnoozProButtonClickedUpdate();
        }

        public async Task AddSnoozProButtonClickedUpdate()
        {
            try
            {
                string product = "SNOOZ Pro";

                UserProducts.Add(product);

                productMenu.UserProducts = UserProducts;

                Label productLabel = new Label
                {
                    Text = product,
                    HorizontalOptions = LayoutOptions.Center,
                    VerticalOptions = LayoutOptions.Center
                };

                productMenu.productsView.Children.Add(productLabel);

                var firebaseUser = new FirebaseUser
                {
                    FirebaseUserEmail = UserEmail,
                    FirebaseUserProducts = UserProducts
                };

                await app.firebaseClient.Child("users").Child(UserUid).PutAsync(firebaseUser);
                await Navigation.PopAsync();
            }
            catch (Exception ex)
            {
                // Handle exceptions
                Console.WriteLine($"Error adding Snooz Pro: {ex.Message}");
            }
        }

        public async void AddBreezButtonClicked(object sender, EventArgs e)
        {
            await AddBreezButtonClickedUpdate();
        }

        public async Task AddBreezButtonClickedUpdate()
        {
            try
            {
                string product = "Breez Smart Bedroom Fan and Sound Machine";

                UserProducts.Add(product);

                productMenu.UserProducts = UserProducts;

                Label productLabel = new Label
                {
                    Text = product,
                    HorizontalOptions = LayoutOptions.Center,
                    VerticalOptions = LayoutOptions.Center
                };

                productMenu.productsView.Children.Add(productLabel);

                var firebaseUser = new FirebaseUser
                {
                    FirebaseUserEmail = UserEmail,
                    FirebaseUserProducts = UserProducts
                };

                await app.firebaseClient.Child("users").Child(UserUid).PutAsync(firebaseUser);
                await Navigation.PopAsync();
            }
            catch (Exception ex)
            {
                // Handle exceptions
                Console.WriteLine($"Error adding Snooz Go: {ex.Message}");
            }
        }
    }
}