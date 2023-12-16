from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.resources import resource_add_path


class AtlasExample(App):
    def build(self):
        # Add the path to your atlas image to the resource search path
        resource_add_path('path/to/your/atlas')

        # Create a BoxLayout
        layout = BoxLayout(orientation='vertical')

        # Create an Image widget using the atlas image
        atlas_image = Image(source='atlas://atlas_name/image_name')

        # Add the Image widget to the layout
        layout.add_widget(atlas_image)

        return layout


if __name__ == '__main__':
    AtlasExample().run()
