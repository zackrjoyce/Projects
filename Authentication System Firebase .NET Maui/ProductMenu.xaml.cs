using Microsoft.Maui.Controls;
using FirebaseAdmin.Auth;
using Firebase.Auth;
using Microsoft.Maui.ApplicationModel.Communication;

namespace MauiTestApp
{
    public partial class ProductMenu : ContentPage
    {
        public string UserUid;
        public string UserEmail;
        public List<string> UserProducts;

        public StackLayout productsView => ProductsView;

        public ProductMenu(string uid,string email, List<string> products)
        {
            InitializeComponent();

            UserUid = uid;
            UserEmail = email;
            UserProducts = products;

            UserInfo.Text = "Logged in as: " + UserEmail;

            foreach(string product in UserProducts)
            {
                Label productLabel = new Label
                {
                    Text = product,
                    HorizontalOptions = LayoutOptions.Center,
                    VerticalOptions = LayoutOptions.Center
                };

                ProductsView.Children.Add(productLabel);
            }
        }

        public async void AddDeviceButtonClicked(object sender, EventArgs e)
        {
            await Navigation.PushAsync(new ProductSelection(UserUid, UserEmail, UserProducts, this));
        }
    }
}